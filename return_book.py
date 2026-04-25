from utils import books,issue_books
def return_books():
    book_name = input("Enter the Name of Book: ").upper()
    if book_name in issue_books :
        issue_books.remove(book_name)
        books.append(book_name)
        print(f"Book Returned : {book_name}")
    else:
        print("Book Not Found... ")
 