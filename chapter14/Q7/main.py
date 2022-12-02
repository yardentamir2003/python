from chapter14.Q7.library import Library
from chapter14.Q7.menu import Menu


def main():
    library = Library()
    library.load_all_from_files()
    menu = Menu()
    menu.add_option("Books Inventory Management", library.show_books_menu)
    menu.add_option("System Readers Management System", library.show_readers_menu)
    menu.show_menu()


main()
