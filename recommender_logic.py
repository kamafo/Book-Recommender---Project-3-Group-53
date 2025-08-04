# recommender_logic.py
from alg1 import load_books, Book

def recommend_books(preferred_genres, preferred_authors):
    books = load_books("books.csv")  # Ensure books.csv is in the same folder

    # Score books based on matches
    for book in books:
        if any(genre.lower() in book.genres for genre in preferred_genres):
            book.score += 1
        if book.author.lower() in [a.lower() for a in preferred_authors]:
            book.score += 1

    # Sort and return top 5
    sorted_books = sorted(books, key=lambda b: (-book.score, -book.rating))
    return sorted_books[:5]
