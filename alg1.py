import csv
import gzip
# algorithm 1: polina antonenko
# basic; based on genre and author

# create Book object class
class Book:
    def __init__(self, title, author, genres, rating):
        self.title = title
        self.author = author
        self.genres = genres
        self.rating = rating
        self.score = 0

# process data from book database (csv file)
def load_books(filename):
    books = []

    # open file
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

            # add Book to the list
            books.append(Book(title, author, genres, rating))
    return books

# score Books based on user input to know what to recommend first
def score_books(books, fav_genres, fav_authors, liked_titles):
    # assign default score
    for book in books:
        score = 0

        # add points for liked author
        if book.author in fav_authors:
            score += 3

        # add points for liked genre
        for genre in book.genres:
            if genre in fav_genres:
                score += 2

        # make sure books user has already listed arent rec options
        if book.title in liked_titles:
            score -= 100

        # save score to Book object
        book.score = score

# sort & recommend highest scored books
def rec_books(books, n):
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
        print(f"{book.title.title()} by {book.author.title()} Score: {book.score} | Rating: {book.rating:.2f}")
        count += 1

        results.append([book.title.title(), book.author.title(), genre, f"{book.rating:.1f}★"])
        
        if count >= n:
            break
    
    return results