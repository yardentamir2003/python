import re


def main():
    get_flight_name()
    get_seat_number()


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


if __name__ == '__main__':
    main()
