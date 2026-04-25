from utils import books, issue_books
def issue_book():
    book_name = input("Enter the Name of Book: ").upper()
    if book_name in books:
        books.remove(book_name)
        issue_books.append(book_name)
        print(f"Book Issued : {book_name}")
    else:
        print("Book Not Available...")
    
    print(f"Total Issued Books: {len(issue_books)}")