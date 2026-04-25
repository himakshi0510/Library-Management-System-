from utils import books, issue_books
def issue_book():
    book_name = input("Enter the Name of Book: ").upper()
    if book_name in books and books[book_name]["student_name"] is None:
        student_name = input("Enter Student's Name: ")
        days = int(input("Enter Number of Days: "))
        books[book_name]["student_name"] = student_name
        books[book_name]["days"] = days
        print(f"{book_name} Issued to {student_name} for {days} days.")
    else:
        print("Book Not Available...")
    
   