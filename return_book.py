from utils import books
def return_books():
    book_name = input("Enter the Name of Book: ").upper()
    if book_name in books and books[book_name]["student_name"] is not None:
        allowed_days = books[book_name]["days"]
        actual_days = int(input("Enter Number of Days Book is Taken: "))
        
        if actual_days <= allowed_days :
            print ( "Book Returned on Time...")
        else:
            days_kept = actual_days - allowed_days
            week = (days_kept//7)+1
            fine = week*10
            total_fine = fine * days_kept
            print(f"Book is Returned Late...{total_fine} Rupees Fine will be Imposed on you...")

        books[book_name]["student_name"] = None
        books[book_name]["days"] = 0
    
        print(f"Book Returned : {book_name}")
    else:
        print("Book Not Found... ")
 