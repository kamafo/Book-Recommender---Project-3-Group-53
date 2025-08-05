from flask import Flask, jsonify, render_template, request
from alg1 import load_books, score_books, rec_books
from alg2 import load_books2, score_books_by_desc, recommend_books

app = Flask(__name__)

result_books = [["Book", "Author", "Genre", "Rating★"]
]

def load_data():
    # Load books from CSV and add data to respective array
    all_books = load_books('books.csv.gz')
    books = [book.title for book in all_books]
    authors = list(set(book.author for book in all_books))
    genres = list(set(genre for book in all_books for genre in book.genres))

    a2_all_books = load_books2('books.csv.gz')
    a2_books = [book.title for book in all_books]
    a2_authors = list(set(book.author for book in all_books))
    a2_genres = list(set(genre for book in all_books for genre in book.genres))

    return all_books, books, authors, genres, a2_all_books, a2_books, a2_authors, a2_genres

all_books, books, authors, genres, a2_all_books, a2_books, a2_authors, a2_genres = load_data()

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
    fav_authors = payload.get('authors', [])
    fav_books = payload.get('books', [])
    fav_genres = payload.get('genres', [])
    algorithm = payload.get('algorithm', [])

    if algorithm == 0:
        score_books(all_books, fav_genres, fav_authors, fav_books)
        result_books = rec_books(all_books, 5)

    if algorithm == 1:
        score_books_by_desc(a2_all_books, fav_books)
        result_books = recommend_books(a2_all_books, 5)

    print(algorithm)
    return jsonify(result_books)

if __name__ == '__main__':
    app.run(debug=True)
