import datetime
import json
import re
from pathlib import Path


def main():
    print("Welcome candidate!\nPlease enter the following details:")
    directory = r"C:\Users\yarde\PycharmProjects\FirstProgram\basics\candidates_files\files"
    files_amount = calculate_files_amount(directory)
    if files_amount >= 100:
        print("candidates list is full, try next year.")
        exit(0)
    file_name = r"{}\candidate_{}.json".format(directory, files_amount)
    details = ask_questions()
    with open(file_name, "w") as output_file:
        json.dump(details, output_file, indent=6)


def calculate_files_amount(directory):
    files_amount = 1
    files = Path(directory).glob('*')
    for file in files:
        files_amount += 1
    return files_amount


def ask_questions():
    details = {}
    details["first_name"] = input("What is your first name: ")
    details["last_name"] = input("What is your last name: ")
    birth_date = get_date("Enter your birth date: ")
    details["birth date"] = birth_date
    if under_eighteen(birth_date):
        parent_approval, school_name, grade = questions_for_younger()
        details["parent_approval"] = parent_approval
        details["grade"] = grade
        details["school"] = school_name
    birth_country = input("What is your birth country: ")
    if birth_country != "israel" and birth_country != "Israel":
        israel_entrance, hebrew_speaker = non_israel_function()
        details["israel entrance"] = israel_entrance
        details["hebrew speaker"] = hebrew_speaker
    details["current country"] = input("What is your current country: ")
    details["city"] = input("What is your current city: ")
    details["street"] = input("What is your current street address: ")
    details["birth country"] = birth_country
    details["familiar candidates"] = familiar_candidates()
    return details


def get_date(question):
    while True:
        date = input(question)
        if is_date_valid(date):
            return date
        print("Ahhh.. Are you sure? Please enter date in format yyyy-mm-dd")


def is_date_valid(date):
    match_date = re.findall('^[0-9]{4}-[0-9]{2}-[0-9]{2}$', date)
    if len(match_date) == 0:
        return False
    full_date = match_date[0]
    month = int(full_date[5:7])
    day = full_date[8:]
    days_in_month = {"01": 31, "02": 29, "03": 31, "04": 30, "05": 31, "06": 30, "07": 31, "08": 31,
                     "09": 30, "10": 31, "11": 30, "12": 31}
    if month not in days_in_month:
        return False
    else:
        days_amount = days_in_month[month]
        if days_amount < day or day == "00":
            return False
    return True


def get_answer(question):
    while True:
        answer = input(question)
        if check_yes_no(answer):
            return answer
        print("Ahhh.. Are you sure? Please enter yes or no")


def check_yes_no(answer):
    match_answer = re.findall("^(?:yes|no)$", answer)
    if len(match_answer) == 0:
        return False
    return True


def non_israel_function():
    israel_entrance = get_date("When did you enter to Israel: ")
    hebrew_speaker = get_answer("Do you speak hebrew (yes/no): ")
    return israel_entrance, hebrew_speaker


def under_eighteen(birth_date):
    birth_year = birth_date[:4]
    birth_year = int(birth_year)
    age = datetime.datetime.now().year - birth_year
    if age < 18:
        return True
    return False


def questions_for_younger():
    parent_approval = get_answer("Do we have parents approval (yes/no): ")
    school_name = input("what is your school name: ")
    grade = input("What is your grade: ")
    return parent_approval, school_name, grade


def familiar_candidates():
    candidates_names = []
    knows_candidates = get_answer("Do you know any candidates (yes/no): ")
    if knows_candidates == "yes":
        candidate_name = input("Who do you know: ")
        candidates_names.append(candidate_name)
        while True:
            knows_candidates = get_answer("Do you know any more candidates (yes/no): ")
            if knows_candidates == "yes":
                candidate_name = input("Who do you know: ")
                candidates_names.append(candidate_name)
            else:
                break
    print("Well done. Your registration is complete.")
    if len(candidates_names) == 0:
        return None
    return candidates_names


main()
