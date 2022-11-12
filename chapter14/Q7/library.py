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
        while True:
            number = input("What would you like to do:\n1. Add new book\n2. delete book\n3. Search book\n")
            if valid_number(number):
                if number == "1":
                    self.books.add_book()
                    break
                elif number == "2":
                    self.books.delete_book()
                    break
                else:
                    self.books.search_book()
                    break
            else:
                print("Invalid input, please enter 1/2/3.")

    def show_readers_menu(self):
        while True:
            choice = input(
                "What would you like to do:\n1. Add new reader\n2. Add annual payment for a reader ID\n"
                "3. Show books by reader "
                "name\n4. Search reader ID by name\n"
                "5. List all readers whose subscription is expired\n"
                "6. Borrow book\n7. Return book\n")
            if valid_choice(choice):
                if choice == "1":
                    self.readers.add_reader()
                    break
                elif choice == "2":
                    self.readers.add_payment()
                    break
                elif choice == "3":
                    self.readers.list_reader_books()
                    break
                elif choice == "4":
                    self.readers.list_id_by_name()
                    break
                elif choice == "5":
                    self.readers.list_expired()
                    break
                elif choice == "6":
                    self.readers.start_borrow_book(self.books)
                    self.books.save_to_file()
                    self.readers.save_to_file()
                    break
                elif choice == "7":
                    self.readers.start_return_book(self.books)
                    self.books.save_to_file()
                    self.readers.save_to_file()
                    break
            else:
                print("Please enter a number between 1-7.")

    def load_all_from_files(self):
        self.books.load_from_file()
        self.readers.load_from_file()


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
