from chapter14.Q7.books import Books
from chapter14.Q7.readers import Readers


class Library:
    def __init__(self):
        books_manager = Books()
        readers_manager = Readers()
        self.books = books_manager
        self.readers = readers_manager

    def show_books_menu(self):
        pass

    def show_readers_menu(self):
        pass
