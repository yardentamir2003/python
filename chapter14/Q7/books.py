import re
from chapter14.Q7.book import Book


class Books:
    def __init__(self):
        self.books = []

    def add_book(self):
        book_name = input("Enter book name: ")
        for book in self.books:
            if book_name == book.name:
                print('The book "{}", already exists.'.format(book_name))
                return
        author_name = input("Enter author name: ")
        while True:
            copies_number = input("Enter number of copies: ")
            if valid_copies_number(copies_number):
                break
            else:
                print("Please enter a numeric input between 0-1000.")
        while True:
            shelf_number = input("Enter book shelf number: ")
            if valid_shelf_number(shelf_number):
                break
            else:
                print("Please enter a year in format XD.")
        reader = None
        book = Book(book_name, author_name, copies_number, shelf_number, reader)
        self.books.append(book)
        print('The book "{}", was added successfully.'.format(book.name))

    def delete_book(self):
        while True:
            if len(self.books) == 0:
                print("The books list is empty. Can't delete books.")
                return
            deleted_book = input("Which book would you like to delete: ")
            for book in self.books:
                if deleted_book == book.name:
                    delete_copies(book)
                    return
                else:
                    print('The book "{}", does not exist in the books list.'.format(deleted_book))
                    return

    def search_book(self):
        while True:
            option = input("search by:\n1. book name\n2. author name\n")
            if valid_option(option):
                break
            else:
                print("Invalid input, please enter 1/2.")
        if option == "1":
            self.search_by_name()
        else:
            self.search_by_author()

    def search_by_name(self):
        book_name = input("Enter book name: ")
        for book in self.books:
            if book.name == book_name:
                print_book_location(book)
                return book

    def search_by_author(self):
        author_name = input("Enter author name: ")
        books_by_author = []
        for book in self.books:
            if book.author_name == author_name:
                books_by_author.append(book)
        if len(books_by_author) == 0:
            print("Books by {}, weren't found.")
        elif len(books_by_author) == 1:
            matching_book = books_by_author[0]
            print_book_location(matching_book)
        else:
            for book in books_by_author:
                print(book.name)
            while True:
                selected_book = input("Choose book: ")
                if selected_book in books_by_author:
                    break
                print("Please choose a book from the list above.")
            index = 0
            for book in books_by_author:
                if selected_book == book.name:
                    break
                else:
                    index += 1
            matching_book = books_by_author[index]
            print_book_location(matching_book)

    def ask_for_book(self):
        while True:
            book = self.search_by_name()
            if book is not None:
                break
            print("The book was not found.")
        return book


def print_book_location(book):
    if book.shelf_number is not None:
        print('The book "{}", is currently on shelf number {}'.format(book.name, book.shelf_number))
    else:
        print('The book "{}", is currently used by {}'.format(book.name, book.reader))


def delete_copies(book):
    if book.copies == "0":
        print("Error, this book has 0 copies.")
    if book.copies == "1":
        book.copies = 0
        print('Ok, book "{}" has 0 copies now.'.format(book.name))
        return
    while True:
        deleted_copies = input(
            'The book "{}", has {} copies. How many copies would you like to delete: '.format(book.name, book.copies))
        if not deleted_copies.isnumeric():
            print("Please enter a numeric input.")
        if int(deleted_copies) > int(book.copies):
            print("Please enter number up to {}.".format(book.copies))
        else:
            book.copies = int(book.copies) - int(deleted_copies)
            book.copies = str(book.copies)
            if book.copies == "1":
                print('Ok, book "{}" has {} copy now.'.format(book.name, book.copies))
            else:
                print('Ok, book "{}" has {} copies now.'.format(book.name, book.copies))
            return


def valid_shelf_number(shelf_number):
    match = re.findall('^[A-H][1-9]$', shelf_number)
    if len(match) == 0:
        return False
    return True


def valid_copies_number(copies_number):
    match = re.findall('^([1-9]\\d{0,2}|1000|0)$', copies_number)
    if len(match) == 0:
        return False
    return True


def valid_option(option):
    match = re.findall("^[12]$", option)
    if len(match) == 0:
        return False
    return True
