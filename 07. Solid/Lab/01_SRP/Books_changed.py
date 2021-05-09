class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return f"{self.author} - {self.title}"


class Person:
    def __init__(self, name):
        self.name = name


class ReaderStatus(Person):
    def __init__(self, book, name):
        super().__init__(name)
        self.book = book
        self.page = 0

    def turn_page(self, page):
        self.page = page

    def print_status(self):
        print(f"{self.name} is on {self.page} page on book {self.book.title}")


class Library:
    def __init__(self, location):
        self.location = location
        self.books = []

    def find_book(self, title):
        book = [book for book in self.books if book.title == title]

        if not book:
            return "Book not found"

        return book[0]

    def add_book(self, book):
        self.books.append(book)
