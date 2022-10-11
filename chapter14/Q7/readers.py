import json
from random import randint
from chapter14.Q7.reader import Reader
import datetime
from datetime import datetime
from datetime import date
import os.path


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
        books = []
        reader = Reader(serial_num, name, registration_date, books)
        self.readers.append(reader)
        self.save_to_file()
        print("Reader {} ({}), was added successfully.".format(name, serial_num))

    def add_payment(self):
        expired_list = self.create_expired_list()
        if len(expired_list) == 0:
            print("All subscriptions are operative.")
            return
        print("Readers that must pay in order to renew their subscription are:")
        for reader in expired_list:
            print(reader)
        while True:
            paying_reader = input("Who is paying?")
            if paying_reader not in expired_list:
                print("Please choose reader from the list above.")
            else:
                expired_list.remove(paying_reader)
                print("{} renewed subscription successfully.".format(paying_reader))
                return expired_list

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
        expired_list = self.create_expired_list()
        if len(expired_list) == 0:
            print("Readers whose subscription is expired weren't found.")
        else:
            print("Readers whose subscription is expired are:")
            for name in expired_list:
                print(name)

    def create_expired_list(self):
        expired_list = []
        today = date.today()
        today_str = today.strftime("%d/%m/%Y")
        for reader in self.readers:
            d1 = datetime.strptime(today_str, "%d/%m/%Y")
            d2 = datetime.strptime(reader.registration_date, "%d/%m/%Y")
            delta = d2 - d1
            if int(delta.days) >= 365:
                expired_list.append(reader.name)
        return expired_list

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
        expired_list = self.create_expired_list()
        reader = self.ask_for_reader()
        if reader.name in expired_list:
            print("Reader can't borrow book. subscription will expire in less than a month.")
        reader.borrow_book_for_reader(books_manager)
        self.save_to_file()

    def start_return_book(self, books_manager):
        reader = self.ask_for_reader()
        reader.return_book_for_reader(books_manager)
        self.save_to_file()

    def save_to_file(self):
        jsons_list = []
        for reader in self.readers:
            jsons_list.append(reader.get_json())
        with open("readers.json", "w") as file:
            json.dump(jsons_list, file)

    def load_from_file(self):
        if os.path.isfile("readers.json"):
            with open("readers.json", "r") as file:
                json_list = json.load(file)
            for item in json_list:
                serial_num = item["serial_num"]
                name = item["name"]
                registration_date = item["registration_date"]
                books = item["books"]
                reader = Reader(serial_num, name, registration_date, books)
                self.readers.append(reader)
        else:
            self.readers = []


def create_serial_num():
    range_start = 10 ** 6
    range_end = (10 ** 7) - 1
    return randint(range_start, range_end)
