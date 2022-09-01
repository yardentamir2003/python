import re
from chapter14.Q7.books import Books


def main():
    while True:
        option = input(
            "What would you like to manage:\n1. Books Inventory Management\n2. System Readers Management System")
        if valid_option(option):
            if option == "1":
                books_inventory_management()
            else:
                system_readers_management_system()
        else:
            print("Invalid input, please enter 1/2.")


def valid_option(option):
    match = re.findall("^[12]$", option)
    if len(match) == 0:
        return False
    return True


def valid_number(number):
    match = re.findall("^[123]$", number)
    if len(match) == 0:
        return False
    return True


def books_inventory_management():
    books = Books()
    number = input("What would you like to do:\n1. Add new book\n2. delete book\n3. Search book")
    if valid_number(number):
        if number == "1":
            books.add_book()
        elif number == "2":
            books.delete_book()
        else:
            books.search_book()
    else:
        print("Invalid input, please enter 1/2/3.")


def system_readers_management_system():
    pass
