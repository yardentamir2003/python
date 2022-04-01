import json
import re


def main():
    files_amount = 0
    print("Welcome candidate!\nPlease enter the following details:")
    file_name = cadidate_XXX.json
    json_file = open("cadidate_XXX.json")

    first_name = input("What is your first name: ")
    last_name = input("What is your last name: ")
    while True:
        birthday_date = input("What is your birth date: ")
        x = check_date(birthday_date)
        if x is None:
            continue
    birth_country = input("What is your birth country: ")
    if birth_country == "israel" or "Israel":
        israel_functuon()
    courrent_country = input("What is your current country: ")
    city =input("What is your current city: ")
    street = input("What is your current street address: ")
    knows_candidats()


def check_date(date):
match_date = re.findall('^[0-9]{4}-[0-9]{2}-[0-9]{2}$', date)
if len(match_date) == 0:
    print("Ahhh.. Are you sure? Please enter date in format yyyy-mm-dd")
    return None
else:
    return False


def israel_function():
    while True:
        israel_entrance = input("When did you enter to Israel: ")
        x = check_date(israel_entrance)
        if x is None:
            continue
    hebrew_speaker = input("Do you speak hebrew (yes/no): ")
    while True:
        yes_no = re.findall('"yes"|"no"', hebrew_speaker)
        if len(yes_no) == 0:
            print("Ahhh.. Are you sure? Please enter yes or no")
            return None
        else:
            return False

def knows_candidats():
    know_candidates = input("Do you know any candidates (yes/no): ")
    while True:
        yes_no = re.findall('"yes"|"no"', know_candidates)
        if len(yes_no) == 0:
            print("Ahhh.. Are you sure? Please enter yes or no")
            return None
        else:
            return False

main()