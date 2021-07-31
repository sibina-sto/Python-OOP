# Ines

class Book:
    def __init__(self, title, author, total_pages):
        self.title = title
        self.author = author
        self.location = location
        self.total_pages = total_pages


class Library:
    def __init__(self, location):
        self.location = location
        self.books = []

    def find_book(self, title):
        try:
            book = [b for b in self.books if b.title == title]
            return book
        except:
            return "No such book"

    def add_book(self, book):
        self.books.append(book)


class Person:
    def __init__(self, name):
        self.name = name


class Reader(Person):
    def __init__(self, name, current_book):
        Person.__init__(self, name)
        self.current_book = current_book
        self.current_page = None

    def turn_page(self, page):
        if self.current_page:
            self.current_page += 1
            return
        self.current_page = 1
