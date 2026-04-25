from utils import books
def show_books():
    if len(books)==0:
        print("No Books are Available")
    else:
        print("books Available... ")
        for book in books:
            print(book)

    print(f"\nTotal Books Available: {len(books)}")
    