from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
authors = [
    "Jane Austen", "George Orwell", "Mark Twain", "J.K. Rowling", "Ernest Hemingway",
    "F. Scott Fitzgerald", "Leo Tolstoy", "Virginia Woolf", "Agatha Christie", "Charles Dickens",
    "Haruki Murakami", "Stephen King", "J.R.R. Tolkien", "C.S. Lewis", "Chinua Achebe",
    "Gabriel García Márquez", "Franz Kafka", "Toni Morrison", "Fyodor Dostoevsky", "Ray Bradbury",
    "Isaac Asimov", "Kurt Vonnegut", "Margaret Atwood", "Emily Dickinson", "Homer",
    "Herman Melville", "James Joyce", "Zora Neale Hurston", "Oscar Wilde", "Sylvia Plath"
]
genres = [
    "Fantasy", "Science Fiction", "Mystery", "Thriller", "Romance",
    "Historical Fiction", "Horror", "Adventure", "Young Adult", "Dystopian",
    "Literary Fiction", "Biography", "Memoir", "Self-Help", "Philosophy",
    "Poetry", "Graphic Novel", "Short Stories", "Crime", "Humor"
]

books = [
    "The Hobbit", "Dune", "The Girl with the Dragon Tattoo", "Gone Girl", "Pride and Prejudice",
    "The Book Thief", "Dracula", "Treasure Island", "The Fault in Our Stars", "The Hunger Games",
    "The Catcher in the Rye", "Steve Jobs", "Educated", "The Power of Now", "Meditations",
    "The Sun and Her Flowers", "Maus", "Tenth of December", "The Silence of the Lambs", "Bossypants"
]

result_books = [["Book", "Author", "Genre", "Rating★"],
    ["The Great Gatsby", "F. Scott Fitzgerald", "Classic", "4.5★"]
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello')
def hello():
    return jsonify({'message': 'Hello, you pressed a button!'})

@app.route('/get_authors')
def get_authors():
    return jsonify(authors)

@app.route('/get_books')
def get_books():
    return jsonify(books)

@app.route('/get_genres')
def get_genres():
    return jsonify(genres)

@app.route('/get_result_books', methods = ['POST'])
def get_result_books():
    payload = request.get_json(force=True)
    authors = payload.get('authors', [])
    books = payload.get('books', [])
    genres = payload.get('genres', [])
    print(authors)
    print(books)
    print(genres)
    return jsonify(result_books)

if __name__ == '__main__':
    app.run(debug=True)
