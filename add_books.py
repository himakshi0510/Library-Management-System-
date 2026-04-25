from utils import books

def add_books():
    book_name = input("Enter the Book Name to Add: ").upper()
    if book_name in books:
        print("Book Already Available...")
    else:
        books[book_name] = {
            "student_name": None,
            "days" :0
        }
        print(f"Book Added : {book_name}")

