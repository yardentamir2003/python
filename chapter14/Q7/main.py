import re
from chapter14.Q7.books import Books
from chapter14.Q7.readers import Readers


def main():
    books_manager = Books()
    readers_manager = Readers()
    books_manager.load_from_file()
    while True:
        number = input(
            "What would you like to manage:\n1. Books Inventory Management\n2. System Readers Management System\n"
            "3. quit\n")
        if valid_number(number):
            if number == "1":
                books_inventory_management(books_manager)
            elif number == "2":
                system_readers_management_system(readers_manager, books_manager)
            else:
                print("Ok, have a good one!")
                return
        else:
            print("Invalid input, please enter 1/2/3.")


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


def books_inventory_management(books_manager):
    number = input("What would you like to do:\n1. Add new book\n2. delete book\n3. Search book\n")
    if valid_number(number):
        if number == "1":
            books_manager.add_book()
        elif number == "2":
            books_manager.delete_book()
        else:
            books_manager.search_book()
    else:
        print("Invalid input, please enter 1/2/3.")


def system_readers_management_system(readers_manager, books_manager):
    choice = input(
        "What would you like to do:\n1. Add new reader\n2. Add annual payment for a reader ID\n"
        "3. Show books by reader "
        "name\n4. Search reader ID by name\n"
        "5. List all readers whose subscription will expire in less than a month\n"
        "6. Borrow book\n7. Return book\n")
    if valid_choice(choice):
        if choice == "1":
            readers_manager.add_reader()
        elif choice == "2":
            pass
        elif choice == "3":
            readers_manager.list_reader_books()
        elif choice == "4":
            readers_manager.list_id_by_name()
        elif choice == "5":
            readers_manager.list_expired()
        elif choice == "6":
            readers_manager.start_borrow_book(books_manager)
        elif choice == "7":
            readers_manager.start_return_book(books_manager)
    else:
        print("Please enter a number between 1-7.")


main()
