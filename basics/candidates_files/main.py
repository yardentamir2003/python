import json
import re


def main():
    print("Welcome candidate!\nPlease enter the following details:")
    files_amount = 001
    for file in files:
        if files_amount > 100:
            print("candidates list is full, try next year.")
            exit(0)
        file_name = "cadidate_{}.json".format(files_amount)
        ask_questions()
        files_amount += 1

def build_dictionary():
    d={}
    d["first name"] = first_name
    d["last name"] = last_name
    d["birth day"] = birth_date
    d["parent_approval"] = parent_approval
    d["grade"] = grade
    d["school"] = school
    d["birth country"] = birth_country
    d["israel entrance"] = israel_entrance
    d["hebrew speaker"] = hebrew_speaker
    d["courrent country"] = courrent_country
    d["city"] = city
    d["street"] = street
    d["familiar candudates"] = candidate_name




def ask_questions():
    first_name = input("What is your first name: ")
    last_name = input("What is your last name: ")
    while True:
        birth_date = input("What is your birth date: ")
        invalid_date = check_date(birth_date)
        if invalid_date is None:
            continue
        if not invalid_date:
            break
    under_eighteen(birth_date)
    birth_country = input("What is your birth country: ")
    if birth_country != "israel" and birth_country != "Israel":
        non_israel_function()
    courrent_country = input("What is your current country: ")
    city = input("What is your current city: ")
    street = input("What is your current street address: ")
    knows_candidates()


def check_date(date):
    match_date = re.findall('^[0-9]{4}-[0-9]{2}-[0-9]{2}$', date)
    if len(match_date) == 0:
        print("Ahhh.. Are you sure? Please enter date in format yyyy-mm-dd")
        return None
    else:
        return False


def check_yes_no(question):
    match_answer = re.findall("^(?:yes|no)$", question)
    if len(match_answer) == 0:
        print("Ahhh.. Are you sure? Please enter yes or no")
        return None
    else:
        return False


def non_israel_function():
    while True:
        israel_entrance = input("When did you enter to Israel: ")
        invalid_date = check_date(israel_entrance)
        if invalid_date is None:
            continue
        if not invalid_date:
            break
    while True:
        hebrew_speaker = input("Do you speak hebrew (yes/no): ")
        invalid_answer = check_yes_no(hebrew_speaker)
        if invalid_answer is None:
            continue
        if not invalid_answer:
            return False


def under_eighteen(birthday_date):
    year = birthday_date[:4]
    year = int(year)
    if year > 2004:
        while True:
            parent_approval = input("Do we have parents approval (yes/no): ")
            invalid_answer = check_yes_no(parent_approval)
            if invalid_answer is None:
                continue
            if not invalid_answer:
                return False
        school_name = input("what is your school name: ")
        grade = input("What is your grade: ")


def knows_candidates():
    while True:
        know_candidates = input("Do you know any candidates (yes/no): ")
        invalid_answer = check_yes_no(know_candidates)
        if invalid_answer is None:
            continue
        if not invalid_answer:
            if know_candidates == "yes":
                candidate_name = input("Who do you know: ")
                continue
            else:
                print("Well done. Your registration is complete.")
                break


main()