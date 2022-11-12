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
            print(reader.name)
        while True:
            paying_reader_num = input("Enter the paying reader's serial number: ")
            for reader in expired_list:
                if reader.serial_num == paying_reader_num:
                    expired_list.remove(reader)
                    today = date.today()
                    registration_date = today.strftime("%d/%m/%Y")
                    reader.registration_date = registration_date
                    self.save_to_file()
                    print("Subscription renewed successfully.")
                    return
                else:
                    print("Please choose reader from the list above.")

    def list_reader_books(self):
        reader_serial_num = int(input("Enter reader's serial number: "))
        for reader in self.readers:
            if reader_serial_num == reader.serial_num:
                reader.list_books()
                return
        print("Reader {} wasn't found.".format(reader_serial_num))

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
            for reader in expired_list:
                print(reader.name, reader.serial_num)

    def create_expired_list(self):
        expired_list = []
        today = date.today()
        today_str = today.strftime("%d/%m/%Y")
        for reader in self.readers:
            d1 = datetime.strptime(today_str, "%d/%m/%Y")
            d2 = datetime.strptime(reader.registration_date, "%d/%m/%Y")
            delta = d1 - d2
            if int(delta.days) >= 365:
                expired_list.append(reader)
        return expired_list

    def ask_for_reader(self):
        while True:
            reader = self.search_reader_by_name()
            if reader is not None:
                return reader
            print("Reader was not found.")

    def ask_for_reader_id(self):
        while True:
            serial_num = input("Enter reader's serial number: ")
            for reader in self.readers:
                if serial_num == str(reader.serial_num):
                    return reader
            print("Serial number was not found.")

    def search_reader_by_name(self):
        reader_name = input("Enter reader name or part of it: ")
        match_list = []
        for reader in self.readers:
            if reader_name == reader.name:
                return reader
            if reader_name in reader.name:
                match_list.append(reader)
        if len(match_list) == 1:
            return match_list[0]
        else:
            reader = choose_specific_reader(match_list)
            return reader

    def start_borrow_book(self, books_manager):
        expired_list = self.create_expired_list()
        reader = self.ask_for_reader_id()
        if reader.name in expired_list:
            print("Reader can't borrow book. subscription is expired.")
            return
        reader.borrow_book_for_reader(books_manager)

    def start_return_book(self, books_manager):
        reader = self.ask_for_reader()
        reader.return_book_for_reader(books_manager)

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


def choose_specific_reader(match_list):
    for reader in match_list:
        print(reader.name)
    while True:
        specific_reader = input("Choose a reader.")
        for reader in match_list:
            if specific_reader == reader.name:
                return reader
        print("Please choose from the list above.")
