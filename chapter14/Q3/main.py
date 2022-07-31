import re
from chapter14.Q3.actors import Actors


def main():
    actors = Actors()
    while True:
        option = input(
            "1. List actors by age\n2. Add actor\n3. Delete actor\n4. Delete movie\n5. Quit\nChoose option: ")
        if valid_option(option):
            if option == "1":
                actors.list_by_age()
                continue
            if option == "2":
                actors.add_actor()
                continue
            if option == "3":
                actors.delete_actor()
                continue
            if option == "4":
                actors.delete_movie()
                continue
            if option == "5":
                print("OK, have a good one!")
                break
        else:
            print("Invalid input, please enter 1/2/3/4/5")


def valid_option(option):
    match = re.findall('^[12345]$', option)
    if len(match) == 0:
        return False
    return True


main()
