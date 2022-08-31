import re
from chapter14.Q7.book import Book


class Books:
    def __init__(self):
        self.books = []

    def add_book(self):
        book_name = input("Enter book name: ")
        for book in self.books:
            if book_name == book.name:
                print('The book "{}" already exist.'.format(book_name))
                return
        author_name = input("Enter author name: ")
        while True:
            copies_number = input("Enter number of copies: ")
            if valid_copies_number(copies_number):
                break
            else:
                print("Please enter a numeric input.")
        while True:
            shelf_number = input("Enter book shelf number: ")
            if valid_book_shelf_number(shelf_number):
                break
            else:
                print("Please enter a year in format XD.")
        reader = None
        book = Book(book_name, author_name, copies_number, shelf_number, reader)
        self.books.append(book)

    def delete_book(self):
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
        pass


def valid_book_shelf_number(shelf_number):
    match = re.findall('^[A-H][1-8]$', shelf_number)
    if len(match) == 0:
        return False
    return True


def valid_copies_number(copies_number):
    match = re.findall('^([1-9][0-9]{0,2}|1000)$', copies_number)
    if len(match) == 0:
        return False
    return True
