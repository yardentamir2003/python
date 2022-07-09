import datetime
import re
from actor import Actor


def main():
    while True:
        option = input("1. List actors by age\n2. Add actor\n3. Delete actor\n4. Delete movie\n5. Quit\nChoose option: ")
        if valid_option(option):
            # if option == "1":
            #     option_one()
            if option == "2":
                option_two()
            # if option == "3":
            #     option_three()
            # if option == "4":
            #     option_four()
            if option == "5":
                print("OK, have a good one!")
                break
            else:
                print("Invalid input, please enter 1/2/3/4")


def valid_option(option):
    match = re.findall('^[12345]$', option)
    if len(match) == 0:
        return False
    return True


def option_two():
    actor_name = input("Enter the actor’s name: ")
    while True:
        actor_birth_year = input("Enter the actor’s birth year: ")
        if valid_birth_year(actor_birth_year):
            break
    actor_age = calculate_age(actor_birth_year)


def calculate_age(actor_birth_year):
    birth_year = int(actor_birth_year)
    age = datetime.datetime.now().year - birth_year
    print(age)
    return age


def valid_birth_year(actor_birth_year):
    match = re.findall('^\d{4}$', actor_birth_year)
    if len(match) == 0:
        return False
    return True

main()