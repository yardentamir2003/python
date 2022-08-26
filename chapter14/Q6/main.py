import re
from os import path
from chapter14.Q6.minions import Minions


def main():
    minions = Minions()
    while True:
        option = input(
            "1. Add minions from file\n2. Save minions to file\n3. List minions\n4. Assign job"
            "\n5. Report job complete\n6. Quit\nChoose option: ")
        if valid_option(option):
            if option == "1":
                file_name = get_file_name()
                minions.add_minions_from_file(file_name)
                print("Minions from {} were added successfully.".format(file_name))
                continue
            if option == "2":
                file_name = input("Choose a file name: ")
                minions.save_minions_to_file(file_name)
                continue
            if option == "3":
                minions.list_minions()
                continue
            if option == "4":
                minions.assign_job()
                continue
            if option == "5":
                minions.report_job_complete()
                continue
            if option == "6":
                print("OK, have a good one!")
                break
        else:
            print("Invalid input, please enter 1/2/3/4/5/6")


def get_file_name():
    while True:
        file_name = input("Enter file name: ")
        if path.exists(file_name):
            return file_name
        print("Can not find file named {} in directory. Please try again.".format(file_name))


def valid_option(option):
    match = re.findall('^[123456]$', option)
    if len(match) == 0:
        return False
    return True


main()
