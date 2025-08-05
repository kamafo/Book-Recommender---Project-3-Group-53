import csv
import gzip
# algorithm 2; polina antonenko
# more complex; based on word overlap in descriptions (bc database has that)

# create Book object class
class Book:
    def __init__(self, title, author, genres, rating, desc):
        # similar to alg 1 but also has a desc part
        self.title = title
        self.author = author
        self.genres = genres
        self.rating = rating
        self.desc = desc
        self.score = 0

# clean up text & deal w/ database errors (dataset keeps changing ' to â€™)
def clean_text(text):
    text = text.replace("â€™", "'").replace("â€“", "-")
    text = text.lower()
    clean = ''
    for ch in text:
        if ch.isalnum() or ch.isspace():
            clean += ch
        else:
            # replace punctuation w/ a space
            clean += ' '
    return clean

# keep track of word frequency
def get_word_freq(text):
    words = clean_text(text).split()
    freq = {}
    for word in words:
        # skip really short or really common words
        stopwords = {'the', 'and', 'or', 'is', 'with', 'a', 'an', 'to', 'of', 'in'}
        if len(word) <= 2 or word in stopwords:
            continue

        if word not in freq:
            freq[word] = 1
        else:
            freq[word] += 1
    return freq

# load books w/ desc
def load_books2(filename):
    books = []
    with gzip.open(filename, 'rt', encoding='utf-8') as f:
        # skip header/first line
        reader = csv.reader(f)
        next(reader, None)

        # split into parts based on commas
        for parts in reader:
            # skip incomplete &/or broken lines
            if len(parts) < 13:
                continue

            # get specific fields (dataset keeps changing ' to â€™ so that part is fixed)
            # title is column 12
            title = parts[11].strip().replace("â€™", "'")
            # author is column 1, select first author if several
            raw_author = parts[0].strip()
            first_author = raw_author.split(',')[0].strip()
            author = first_author.replace("â€™", "'")
            # genre is column 4
            genre_str = parts[3].strip().replace("â€™", "'")
            # rating is column 10
            rating_str = parts[9].strip()

            # separate genres
            genres = [g.strip() for g in genre_str.split(',') if g.strip()]

            # convert rating to float
            try:
                rating = float(rating_str)
            except:
                # skip if rating =/= a valid num
                continue

            # deal w/ desc
            desc = parts[2].strip().replace("â€™", "'")

            # add Book to the list
            books.append(Book(title, author, genres, rating, desc))
        return books

# score books (compare descriptions to that of liked books)
def score_books_by_desc(books, liked_titles):
    # word freq of liked books
    liked_freq = {}
    for book in books:
        if book.title in liked_titles:
            freq = get_word_freq(book.desc)
            for word in freq:
                if word not in liked_freq:
                    liked_freq[word] = freq[word]
                else:
                    liked_freq[word] += freq[word]

    # compare other book descs w/ this one
    for book in books:
        # assign default score
        score = 0
        book_freq = get_word_freq(book.desc)

        # make sure books user has already listed arent rec options
        if book.title in liked_titles:
            book.score = -100
            continue

        # increase score for similar descriptions
        for word in book_freq:
            if word in liked_freq:
                # weighted match
                score += book_freq[word] * liked_freq[word]
        book.score = score

# sort & rec highest scored books
def recommend_books(books, n):
    # sort in descending order by score & then by rating
    sorted_books = sorted(books, key=lambda b: (-b.score, -b.rating))

    results = []
    # show top n books w/ score > 0
    count = 0
    for book in sorted_books:
        # skip books that arent scored well
        if book.score <= 0:
            continue

        genre = book.genres[0].title() if book.genres else ""

        # format output
        print(f"{book.title.title()} by {book.author.title()} | Score: {book.score} | Rating: {book.rating:.2f}")
        count += 1

        results.append([book.title.title(), book.author.title(), genre, f"{book.rating:.1f}★"])

        if count >= n:
            break
    return results