from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, email):
        self.name = name
        self.email = email

    @abstractmethod
    def role(self):
        pass

    def __str__(self):
        return f"{self.name} - {self.email}"


class Member(Person):
    def __init__(self, name, email, member_id):
        super().__init__(name, email)
        self.member_id = member_id

    def role(self):
        return "Library Member"


class Librarian(Person):
    def role(self):
        return "Library Librarian"


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def __str__(self):
        return f"{self.title} by {self.author}"


class Loan:
    def __init__(self, member, book):
        self.member = member
        self.book = book
        self.active = True

    def borrow(self):
        if self.book.available:
            self.book.available = False
            print("Book borrowed successfully")
        else:
            print("Book is not available")


class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.loans = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def borrow_book(self, member, book):
        loan = Loan(member, book)
        loan.borrow()
        if loan.active and not book.available:
            self.loans.append(loan)


# Create Library
library = Library()

# Create Books
book1 = Book("Python Programming", "John")
book2 = Book("Java Basics", "David")

library.add_book(book1)
library.add_book(book2)

# Create Member
member = Member("Ahmad", "ahmad@gmail.com", 101)

library.add_member(member)

# Create Librarian
librarian = Librarian("Ali", "ali@gmail.com")

# Borrow Book
library.borrow_book(member, book1)

# Polymorphism
people = [member, librarian]

for person in people:
    print(person)
    print("Role:", person.role())

# Display Books
print("\nLibrary Books:")
for book in library.books:
    print(book, "| Available:", book.available)