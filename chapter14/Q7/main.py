import re
from chapter14.Q7.library import Library


def main():
    library = Library()
    library.books.load_from_file()
    library.readers.load_from_file()
    while True:
        number = input(
            "What would you like to manage:\n1. Books Inventory Management\n2. System Readers Management System\n"
            "3. quit\n")
        if valid_number(number):
            if number == "1":
                library.show_books_menu()
            elif number == "2":
                library.show_readers_menu()
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


main()
