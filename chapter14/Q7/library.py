import re
from chapter14.Q7.books import Books
from chapter14.Q7.readers import Readers


class Library:
    def __init__(self):
        books_manager = Books()
        readers_manager = Readers()
        self.books = books_manager
        self.readers = readers_manager

    def show_books_menu(self):
        number = input("What would you like to do:\n1. Add new book\n2. delete book\n3. Search book\n")
        if valid_number(number):
            if number == "1":
                self.books.add_book()
            elif number == "2":
                self.books.delete_book()
            else:
                self.books.search_book()
        else:
            print("Invalid input, please enter 1/2/3.")

    def show_readers_menu(self):
        choice = input(
            "What would you like to do:\n1. Add new reader\n2. Add annual payment for a reader ID\n"
            "3. Show books by reader "
            "name\n4. Search reader ID by name\n"
            "5. List all readers whose subscription will expire in less than a month\n"
            "6. Borrow book\n7. Return book\n")
        if valid_choice(choice):
            if choice == "1":
                self.readers.add_reader()
            elif choice == "2":
                self.readers.add_payment()
            elif choice == "3":
                self.readers.list_reader_books()
            elif choice == "4":
                self.readers.list_id_by_name()
            elif choice == "5":
                self.readers.list_expired()
            elif choice == "6":
                self.readers.start_borrow_book(self.books)
            elif choice == "7":
                self.readers.start_return_book(self.books)
        else:
            print("Please enter a number between 1-7.")


def valid_number(number):
    match = re.findall("^[123]$", number)
    if len(match) == 0:
        return False
    return True


def valid_choice(choice):
    match = re.findall("^[1-7]$", choice)
    if len(match) == 0:
        return False
    return True
