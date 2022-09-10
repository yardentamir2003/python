class Reader:
    def __init__(self, serial_num, name, registration_date):
        self.serial_num = serial_num
        self.name = name
        self.registration_date = registration_date
        self.books = []

    def list_books(self):
        if len(self.books) == 0:
            print("The reader {}, doesn't have books.".format(self.name))
        else:
            for book in self.books:
                print(book)

    def borrow_book(self, book):
        if len(self.books) == 2:
            print("Reader already borrowed 2 books.")
        else:
            self.books.append(book.name)

    def return_book(self):
        pass
