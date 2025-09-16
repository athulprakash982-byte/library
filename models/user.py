class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []
    
    def borrow_book(self, book):
        if len(self.borrowed_books) < 3:  # Max 3 books
            self.borrowed_books.append(book)
            return f"{self.name} borrowed '{book.title}'"
        return "Maximum borrowing limit reached"
    
    def return_book(self, book):  # ← ADD THIS NEW METHOD
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            return f"{self.name} returned '{book.title}'"
        return f"{self.name} doesn't have this book"
    
    def show_borrowed(self):
        if not self.borrowed_books:
            return f"{self.name} has no borrowed books"
        return f"{self.name}'s books: {[book.title for book in self.borrowed_books]}"