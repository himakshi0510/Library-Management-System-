from add_books import add_books
from show_books import show_books
from issue_book import issue_book
from return_book import return_books

def library():
    while True:
        print("\n --OPTIONS:--")
        print("1. Add Book")
        print("2. Show Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")
        choice = (input("Enter Your Choice: "))
        if choice.isdigit():
            choice = int(choice)
        else:
            print("invalid choice...please enter digit only")
            continue
        if choice == 1: add_books()
        elif choice == 2: show_books()
        elif choice == 3: issue_book()
        elif choice == 4: return_books()
        elif choice == 5:
            print("Thankyou")
            break
        else:
            print("Invalid Choice...")

library()