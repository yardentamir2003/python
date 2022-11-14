class Book:
    def __init__(self, book_name, author_name, copies, shelf_number, readers):
        self.name = book_name
        self.author_name = author_name
        self.copies = copies
        self.shelf_number = shelf_number
        self.readers = readers

    def borrow_book(self, reader):
        self.copies -= 1
        self.readers.append(reader.name)
        print("Reader {}, borrowed book '{}'.".format(reader.name, self.name))

    def return_book(self, reader):
        self.copies += 1
        self.shelf_number = "A1"
        print("Reader {}, returned book '{}'.".format(reader.name, self.name))
        self.readers.remove(reader.name)

    def get_json(self):
        return {
            "name": self.name,
            "author_name": self.author_name,
            "copies": self.copies,
            "shelf_number": self.shelf_number,
            "readers": self.readers
        }
