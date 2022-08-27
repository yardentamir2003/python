import re


def main():
    while True:
        option = input("What are you willing to do:\n1. Books Inventory Management\n2. System Readers Management System")
        if valid_option(option):
            if option == "1":
                books_inventory_management()
            else:
                system_readers_managment_system()

        else:
            print("Invalid input, please enter 1/2.")


def valid_option(option):
    match = re.findall("^[12]$", option)
    if len(match) == 0:
        return False
    return True


def books_inventory_management():
    pass


def system_readers_managment_system():
    pass
