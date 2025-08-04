
def display_main_menu():
    print("\nWelcome to the Book Recommender!")
    print("Please choose an option:")
    print("1. Enter Favorite Books")
    print("2. Enter Favorite Genres")
    print("3. Enter Favorite Authors")
    print("4. Rate 5 Books")
    print("5. Get Recommendations")
    print("6. Exit")

def get_favorite_items(prompt):
    print(f"\n{prompt} (Type 'done' when finished):")
    items = []
    while True:
        entry = input(">> ").strip()
        if entry.lower() == 'done':
            break
        elif entry:
            items.append(entry)
    return items

def rate_books():
    ratings = {}
    print("\nRate 5 books (1-5 stars). Type 'skip' to finish early.")
    while len(ratings) < 5:
        book = input(f"Enter book title #{len(ratings)+1}: ").strip()
        if book.lower() == 'skip':
            break
        rating = input(f"Rate '{book}' (1-5): ").strip()
        if rating.isdigit() and 1 <= int(rating) <= 5:
            ratings[book] = int(rating)
        else:
            print("Invalid rating. Please enter a number between 1 and 5.")
    return ratings

def validate_preferences(books, genres, authors, ratings):
    if not (books or genres or authors or ratings):
        print("Error: At least one preference (book, genre, author, or rating) must be provided.")
        return False
    return True

def main():
    favorite_books = []
    favorite_genres = []
    favorite_authors = []
    book_ratings = {}

    while True:
        display_main_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            favorite_books = get_favorite_items("Enter your favorite books")
        elif choice == '2':
            favorite_genres = get_favorite_items("Enter your favorite genres")
        elif choice == '3':
            favorite_authors = get_favorite_items("Enter your favorite authors")
        elif choice == '4':
            book_ratings = rate_books()
        elif choice == '5':
            if not validate_preferences(favorite_books, favorite_genres, favorite_authors, book_ratings):
                continue
            print("\n--- Recommended for You ---")
            print("(*This is where algorithm will generate recommendations*)")
        elif choice == '6':
            print("Thank you for using the Book Recommender. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
