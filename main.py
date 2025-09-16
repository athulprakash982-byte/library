from models.book import Book
from models.user import User
from utils.helpers import format_name

def main():
    print("=== Library Management System ===")
    
    # Create books
    book1 = Book("Python Basics", "John Doe", "123-456")
    book2 = Book("Advanced Python", "Jane Smith", "789-012")
    
    # Create user
    user = User(format_name("alice johnson"), "U001")
    
    # Library operations
    print(book1)
    print(user.borrow_book(book1))
    print(book1.borrow())
    print(user.show_borrowed())
    print(book1.return_book())
    print(user.show_borrowed())

if __name__ == "__main__":
    main()