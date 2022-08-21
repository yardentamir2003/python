import json
import re
from chapter14.Q5.minion import Minion
from os import path


def main():
    minions = []
    while True:
        option = input(
            "1. Add minions from file\n2. Save minions to file\n3. List minions\n4. Assign job"
            "\n5. Report job complete\n6. Quit\nChoose option: ")
        if valid_option(option):
            if option == "1":
                file_name = get_file_name()
                added_minions = add_minions_from_file(file_name)
                minions.extend(added_minions)
                print("Minions from {} were added successfully.".format(file_name))
                continue
            if option == "2":
                save_minions_to_file(minions)
                continue
            if option == "3":
                list_minions(minions)
                continue
            if option == "4":
                assign_job(minions)
                continue
            if option == "5":
                report_job_complete(minions)
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


def add_minions_from_file(file_name):
    with open(file_name, "r") as file:
        minions_list = []
        for line in file:
            line = line.strip()
            m = Minion(line)
            minions_list.append(m)
    return minions_list


def save_minions_to_file(minions):
    file_name = input("Choose a file name: ")
    for minion in minions:
        json_data = Minion.get_json_string(minion)
        with open(file_name, "a") as file:
            line = json.dumps(json_data)
            file.write(line)
            file.write("\n")
    print("file named {}, was created successfully.".format(file_name))


def list_minions(minions):
    for minion in minions:
        print(minion)


def assign_job(minions):
    required_job = input("What is the job? ")
    required_eyes_amount = int(input("How many eyes are required? "))
    match_list = matching_minions(required_eyes_amount, minions)
    if len(match_list) == 0:
        print("No matching minions were found.")
        return
    print("OK, the list of unemployed minions with {} eyes are:".format(required_eyes_amount))
    for minion in match_list:
        print(minion)
    while True:
        selected_minion = input("Type the minion name: ")
        for minion in match_list:
            if minion.name == selected_minion:
                Minion.assign_job(minion, required_job)
                print("OK, {} is now working on job {}".format(selected_minion, required_job))
                return
        print("Please select a minion from the list above.")


def matching_minions(required_eyes_amount, minions):
    match_list = []
    for minion in minions:
        if Minion.is_unemployed(minion) and Minion.is_eyes_amount(minion, required_eyes_amount):
            match_list.append(minion)
    return match_list


def report_job_complete(minions):
    finisher_minion = input("Who completed his job? ")
    for minion in minions:
        if minion.name == finisher_minion:
            if minion.job == "none":
                print("{} is already unemployed.".format(finisher_minion))
                return
            Minion.complete_job(minion)
            print("OK, {} is now unemployed".format(finisher_minion))
    minions_names = []
    for minion in minions:
        minions_names.append(minion.name)
    if finisher_minion not in minions_names:
        print("{} doesn't exist in the minions list.".format(finisher_minion))


main()
