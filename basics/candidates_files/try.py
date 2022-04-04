import json
import re


def main():
    print("Welcome candidate!\nPlease enter the following details:")
    # files_amount = 0o1
    # for file in files:
    # if files_amount > 100:
    # print("candidates list is full, try next year.")
    # exit(0)
    # file_name = "cadidate_{}.json".format(files_amount)
    d = ask_questions()
    # output_file = open(file_name, "w")
    # json.dump(d, output_file, indent=6)
    # files_amount += 1


def ask_questions():
    d = {}
    d["first_name"] = input("What is your first name: ")
    d["last_name"] = input("What is your last name: ")
    birth_date = get_date("Enter your birth date: ")
    d["birth date"] = birth_date
    parent_approval, school_name, grade = under_eighteen(birth_date)
    birth_country = input("What is your birth country: ")
    if birth_country != "israel" and birth_country != "Israel":
        israel_entrance, hebrew_speaker = non_israel_function()
        d["israel entrance"] = israel_entrance
        d["hebrew speaker"] = hebrew_speaker
    d["current country"] = input("What is your current country: ")
    d["city"] = input("What is your current city: ")
    d["street"] = input("What is your current street address: ")
    candidates_names = knows_candidates()
    d["parent_approval"] = parent_approval
    d["grade"] = grade
    d["school"] = school_name
    d["birth country"] = birth_country
    d["familiar candidates"] = candidates_names
    print(d)
    return d


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


def under_eighteen(birthday_date):
    year = birthday_date[:4]
    year = int(year)
    if year > 2004:
        parent_approval = get_answer("Do we have parents approval (yes/no): ")
        school_name = input("what is your school name: ")
        grade = input("What is your grade: ")
        return parent_approval, school_name, grade


def knows_candidates():
    candidates_names = []
    while True:
        knows_candidates = get_answer("Do you know any candidates (yes/no): ")
        if knows_candidates == "yes":
            candidate_name = input("Who do you know: ")
            candidates_names.append(candidate_name)
                    continue
            print("Well done. Your registration is complete.")
            return candidates_names




main()
