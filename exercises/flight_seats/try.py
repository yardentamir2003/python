import re
import pathlib


def get_flight_name():
    while True:
        flight_name = input("Please enter a flight name: ")
        if valid_flight_number(flight_name):
            return flight_name
        print("Please enter flight number in format xxxx-yy-xxxx")


def valid_flight_number(flight_name):
    match_flight_number = re.findall('^[0-9]{4}-[a-z]{2}-[0-9]{4}$', flight_name)
    if len(match_flight_number) == 0:
        return False
    return True


def get_seat_number():
    while True:
        seat_number = input("Please enter a seat number: ")
        if valid_seat_number(seat_number):
            return seat_number
        print("Please enter seat number in format xy")


def valid_seat_number(seat_number):
    match_seat_number = re.findall('^[1-8][a-e]$', seat_number)
    if len(match_seat_number) == 0:
        return False
    return True


def free_seat(file_name, seat_number):
    file = pathlib.Path(file_name)
    if file.exists():
        with open(file_name, "r") as file:
            for line in file:
                line = line.strip()
                if line == seat_number:
                    return False
    return True


def append_to_file(file_name, seat_number):
    with open(file_name, "a") as file:
        if free_seat(file_name, seat_number):
            file.write(seat_number)
            file.write("\n")


def full_flight(file_name):
    file = pathlib.Path(file_name)
    if file.exists():
        with open(file_name, "r") as file:
            line_amount = len(file.readlines())
            if line_amount == 40:
                return True
    return False


def get_flight_file_name():
    while True:
        flight_name = get_flight_name()
        directory = r"C:\Users\yarde\PycharmProjects\python\exercises\flight_seats\flights"
        file_name = r"{}\{}".format(directory, flight_name)
        if not full_flight(file_name):
            return file_name
        print("all seats of the flight have already been reserved, please select another flight.")


def set_seat_in_flight_file(file_name):
    while True:
        seat_number = get_seat_number()
        if free_seat(file_name, seat_number):
            append_to_file(file_name, seat_number)
            print("Your seat has been ordered successfully, Thanks for choosing Jordi Airlines.")
            return
        print("this seat has already been reserved, please select another seat.")


def main():
    file_name = get_flight_file_name()
    set_seat_in_flight_file(file_name)


if __name__ == '__main__':
    main()
