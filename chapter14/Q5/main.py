import re
from chapter14.Q5.minion import Minion


def main():
    # minion = Minion(name, eyes_amount, job)
    while True:
        option = input(
            "1. List actors by age\n2. Add actor\n3. Delete actor\n4. Delete movie\n5. Quit\nChoose option: ")
        if valid_option(option):
            if option == "1":
                add_minions_from_file()
                continue
            if option == "2":
                save_minions_to_file()
                continue
            if option == "3":
                list_minions()
                continue
            if option == "4":
                assign_job()
                continue
            if option == "5":
                report_job_complete()
            if option == "6":
                print("OK, have a good one!")
                break
        else:
            print("Invalid input, please enter 1/2/3/4/5/6")


def get_file_name(file_name):
    with open file asy
        minions_list = []
        for line in file:
            m = Minion(line)
        minions_list.append(m)
    return minions_list

def valid_option(option):
    match = re.findall('^[12345]$', option)
    if len(match) == 0:
        return False
    return True


def add_minions_from_file():
    pass


def save_minions_to_file():
    pass


def list_minions():
    pass


def assign_job():
    required_job = input("What is the job? ")
    required_eyes_amount = input("How many eyes are required? ")
    matcing_minions = matching_minions(required_eyes_amount)
    print("OK, the list of unemployed minions with {} eyes are:\n".format(required_eyes_amount))
    # print(matching_minions)
    selected_minion = input("Type the minion name: ")
    print("OK, {} is now working on job {}".format(selected_minion, required_job))


def report_job_complete():
    pass


main()
