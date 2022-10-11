class Book:
    def __init__(self, book_name, author_name, copies, shelf_number, reader):
        self.name = book_name
        self.author_name = author_name
        self.copies = copies
        self.shelf_number = shelf_number
        self.reader = reader

    def borrow_book(self, reader):
        self.copies -= 1
        self.shelf_number = None
        self.reader = reader.name
        print("Reader {}, borrowed book '{}'.".format(self.reader, self.name))

    def return_book(self):
        self.copies += 1
        self.shelf_number = "A1"
        self.reader = None
        print("Reader {}, returned book '{}'.".format(self.reader, self.name))

    def get_json(self):
        return {
            "name": self.name,
            "author_name": self.author_name,
            "copies": self.copies,
            "shelf_number": self.shelf_number,
            "reader": self.reader
        }
