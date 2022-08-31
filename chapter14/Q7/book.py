class Book:
    def __init__(self, book_name, author_name, copies_number, shelf_number, reader):
        self.name = book_name
        self.author_name = author_name
        self.copies = copies_number
        self.shelf_number = shelf_number
        self.reader = reader

    def borrow_book(self, reader):
        pass

    def return_book(self, reader):
        pass
