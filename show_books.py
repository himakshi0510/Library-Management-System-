from utils import books
def show_books():
    if len(books)==0:
        print("No Books are Available")
    else:
        print("books Available... ")
        for book, details in books.items():
            if details["student_name"] is None :
                print(f"{book} is Available... ")
            else:
                print(f"{book} is issued to {details["student_name"]} for {details["days"]} days... ")

    print(f"\nTotal Books Available: {len(books)}")
    