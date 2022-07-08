import datetime
import re


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
            else:
                print("Invalid input, please enter 1/2/3/4")


def valid_option(option):
    match = re.findall('^[1234]$', option)
    if len(match) == 0:
        return False
    return True


def option_two():
    actor_name = input("Enter the actor’s name: ")
    actor_birth_year = input("Enter the actor’s birth year: ")
    actor_age = calculate_age(actor_birth_year)


def calculate_age(actor_birth_year):
    birth_year = int(actor_birth_year)
    age = datetime.datetime.now().year - birth_year
    print(age)
    return age


main()