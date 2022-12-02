from chapter14.Q7.books import Books
from chapter14.Q7.menu import Menu
from chapter14.Q7.readers import Readers


class Library:
    def __init__(self):
        books_manager = Books()
        readers_manager = Readers()
        self.books = books_manager
        self.readers = readers_manager

    def show_books_menu(self):
        menu = Menu()
        menu.add_option("Add book", self.books.add_book)
        menu.add_option("Delete book", self.books.delete_book)
        menu.add_option("Search book", self.books.search_book)
        menu.show_menu()

    def show_readers_menu(self):
        menu = Menu()
        menu.add_option("Add new reader", self.readers.add_reader)
        menu.add_option("Add annual payment for a reader ID", self.readers.add_payment)
        menu.add_option("Show books by reader", self.readers.list_reader_books)
        menu.add_option("Search reader ID by name", self.readers.list_id_by_name)
        menu.add_option("List all readers whose subscription is expired", self.readers.list_expired())
        menu.add_option("Borrow book", self.all_borrow_book)
        menu.add_option("Return book", self.all_return_book)
        menu.show_menu()

    def all_borrow_book(self):
        self.readers.start_borrow_book(self.books)
        self.books.save_to_file()
        self.readers.save_to_file()

    def all_return_book(self):
        self.readers.start_return_book(self.books)
        self.books.save_to_file()
        self.readers.save_to_file()

    def load_all_from_files(self):
        self.books.load_from_file()
        self.readers.load_from_file()
