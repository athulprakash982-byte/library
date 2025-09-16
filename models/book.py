
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False
    
    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return f"'{self.title}' borrowed successfully"
        return f"'{self.title}' is already borrowed"
    
    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return f"'{self.title}' returned successfully"
        return f"'{self.title}' was not borrowed"
    
    def __str__(self):
        status = "Available" if not self.is_borrowed else "Borrowed"
        return f"'{self.title}' by {self.author} - {status}"