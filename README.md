# Library Management System:

This project is a simple Library Management System built using Python.  
It is a menu-driven program that allows users to manage books in a library.

---

## Features:

- Add Books
- Show Available Books
- Issue Books to Students
- Return Books
- Student Tracking (who issued the book)
- Track number of days
- Fine calculation for late return
- Continuous menu using while loop

---

## Technologies Used:

- Python (Basic Concepts)
- Functions
- Dictionary
- Lists
- Conditional Statements
- Loop (while True)

---

## Project Structure:

library_management/
│
├── main.py            # Menu and user interaction
├── utils.py           # Stores book data
├── add_books.py       # Add book function
├── show_books.py      # Display books
├── issue_book.py      # Issue book to student
└── return_book.py     # Return book and fine calculation

---

## How to Run:

1. Open terminal in project folder  
2. Run:
python main.py

---

## Features Explained:

- Books are stored using a dictionary  
- Each book keeps record of:
  - Student name  
  - Number of days issued  
- Fine is calculated based on late return:
  - Week 1 → ₹10/day  
  - Week 2 → ₹20/day  
  - Week 3 → ₹30/day  

---

## Notes:

- This is a basic project for learning purposes  
- Data is not stored permanently (resets on restart)  
- Designed using modular structure  

---

## Author:

- Himakshi
