from random import randint
from chapter14.Q7.reader import Reader
import datetime
from datetime import datetime, time
from datetime import date


class Readers:
    def __init__(self):
        self.readers = []

    def add_reader(self):
        serial_num_list = []
        while True:
            serial_num = create_serial_num()
            if serial_num not in serial_num_list:
                serial_num_list.append(serial_num)
                break
        name = input("Enter reader's name: ")
        today = date.today()
        registration_date = today.strftime("%d/%m/%Y")
        reader = Reader(serial_num, name, registration_date)
        self.readers.append(reader)
        print("Reader {} ({}), was added successfully.".format(name, serial_num))

    def add_payment(self):
        # add all readers whose subscription will expire in less than a month to pay_list. choose a reader,
        # pay and remove him from the list.
        pass

    def list_reader_books(self):
        reader_name = input("Enter reader's name: ")
        for reader in self.readers:
            if reader_name == reader.name:
                reader.list_books()
                return
        print("Reader {} wasn't found.".format(reader_name))

    def list_id_by_name(self):
        match_list = []
        reader_name = input("Enter reader's name or part of it: ")
        for reader in self.readers:
            if reader_name in reader.name:
                match_list.append("{} {}".format(reader.name, reader.serial_num))
        if len(match_list) == 0:
            print("Readers weren't found.")
        else:
            for item in match_list:
                print(item)

    def list_expired(self):
        # check if subscription will expire in less than a month.
        expired_list = []
        today = date.today()
        today_str = today.strftime("%d/%m/%Y")
        for reader in self.readers:
            d1 = datetime.strptime(today_str, "%Y/%m/%d")
            d2 = datetime.strptime(reader.registration_date, "%Y/%m/%d")
            delta = d2 - d1
            if delta.days >= 335:
                expired_list.append(reader.name)
        if len(expired_list) == 0:
            print("Readers whose subscription will expire in less than a month weren't found.")
        else:
            print("Readers whose subscription will expire in less than a month are:")
            for name in expired_list:
                print(name)

    def ask_for_reader(self):
        while True:
            reader = self.search_reader_by_name()
            if reader is not None:
                return reader
            print("Reader was not found.")

    def search_reader_by_name(self):
        reader_name = input("Enter reader name: ")
        for reader in self.readers:
            if reader_name == reader.name:
                return reader

    def start_borrow_book(self, books_manager):
        # don't allow borrow book if subscription will expire in less than a month.
        reader = self.ask_for_reader()
        reader.borrow_book_for_reader(books_manager)

    def start_return_book(self, books_manager):
        reader = self.ask_for_reader()
        reader.return_book_for_reader(books_manager)


def create_serial_num():
    range_start = 10 ** 6
    range_end = (10 ** 7) - 1
    return randint(range_start, range_end)
