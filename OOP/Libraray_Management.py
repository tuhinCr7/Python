class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def __str__(self):
        status = "Available" if self.is_available else "Borrowed"
        return f"{self.title} by {self.author} | ISBN: {self.isbn} | {status}"


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            print(f"{self.name} cannot borrow more than 3 books.")
            return False
        
        self.borrowed_books.append(book)
        return True

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            return True
        return False


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def issue_book(self, member_id, isbn):
        member = self.find_member(member_id)
        book = self.find_book(isbn)

        if not member:
            print("Member not found.")
            return
        
        if not book:
            print("Book not found.")
            return
        
        if not book.is_available:
            print("Book is already borrowed.")
            return

        if member.borrow_book(book):
            book.is_available = False
            print(f"Book '{book.title}' issued to {member.name}.")

    def return_book(self, member_id, isbn):
        member = self.find_member(member_id)
        book = self.find_book(isbn)

        if not member:
            print("Member not found.")
            return
        
        if not book:
            print("Book not found.")
            return

        if member.return_book(book):
            book.is_available = True
            print(f"Book '{book.title}' returned by {member.name}.")
        else:
            print("This member did not borrow this book.")

    def display_books(self):
        print("\nLibrary Books:")
        for book in self.books:
            print(book)
library = Library()

book1 = Book("Python Basics", "John Doe", "123")
book2 = Book("AI Intro", "Jane Smith", "456")

member1 = Member("Tuhin", "M001")

library.add_book(book1)
library.add_book(book2)
library.add_member(member1)

library.issue_book("M001", "123")
library.issue_book("M001", "456")

library.display_books()

library.return_book("M001", "123")

library.display_books()            
             