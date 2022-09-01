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
                print("Please enter a numeric input between 1-1000.")
        while True:
            shelf_number = input("Enter book shelf number: ")
            if valid_shelf_number(shelf_number):
                break
            else:
                print("Please enter a year in format XD.")
        reader = None
        book = Book(book_name, author_name, copies_number, shelf_number, reader)
        self.books.append(book)

    def delete_book(self):
        # can delete a copy or all copies!
        while True:
            if len(self.books) == 0:
                print("The books list is empty. Can't delete books.")
                return
            deleted_book = input("Which book would yoe like to delete: ")
            for book in self.books:
                if deleted_book == book.name:
                    self.books.remove(book)
                    print('OK, the book "{}" was deleted'.format(deleted_book))
                    return
            print('"{}" does not exist in the books list.'.format(deleted_book))

    def search_book(self):
        while True:
            option = input("search by:\n1. book name\n2. author name")
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
                if book.shelf_number is not None:
                    print('The book "{}", is currently on shelf number {}'.format(book_name, book.shelf_number))
                else:
                    print('The book "{}", is currently used by {}'.format(book_name, book.reader))

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
            if matching_book.shelf_number is not None:
                print('The book "{}", is currently on shelf number {}'.format(matching_book.name, matching_book.shelf_number))
            else:
                print('The book "{}", is currently used by {}'.format(matching_book.name, matching_book.reader))
        else:


def valid_shelf_number(shelf_number):
    match = re.findall('^[A-H][1-9]$', shelf_number)
    if len(match) == 0:
        return False
    return True


def valid_copies_number(copies_number):
    match = re.findall('^([1-9][0-9]{0,2}|1000)$', copies_number)
    if len(match) == 0:
        return False
    return True


def valid_option(option):
    match = re.findall("^[12]$", option)
    if len(match) == 0:
        return False
    return True
