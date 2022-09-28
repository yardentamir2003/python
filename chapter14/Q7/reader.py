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

    def borrow_book_for_reader(self, books_manager):
        book = books_manager.ask_for_book()
        if len(self.books) == 2:
            print("Reader already borrowed 2 books.")
        else:
            self.books.append(book)
            book.borrow_book(self)

    def return_book(self):
        pass
