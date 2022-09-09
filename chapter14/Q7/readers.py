from random import randint
from datetime import date
from chapter14.Q7.reader import Reader


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
        pass

    def list_reader_books(self):
        reader_name = input("Enter reader's name: ")
        for reader in self.readers:
            if reader_name == reader.name:
                reader.list_books()
                return
        print("Reader {} wasn't found.".format(reader_name))

    def list_id_by_name(self):
        reader_name = input("Enter reader's name: ")
        for reader in self.readers:
            if reader_name == reader.name:
                print(reader.serial_num)
                return
        print("Reader {} wasn't found.".format(reader_name))

    def list_expired(self):
        pass

    def borrow_book(self, book):
        pass

    def return_book(self):
        pass


def create_serial_num():
    range_start = 10 ** 6
    range_end = (10 ** 7) - 1
    return randint(range_start, range_end)
