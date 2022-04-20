import re


def main():
    while True:
        option_number = get_option_number()
        if option_number == "3":
            break
        if option_number == "1":
            solve_exercises()
        if option_number == "2":
            ...


def get_option_number():
    while True:
        option_number = input("1. Solve exercises\n2. Check exercises\n3. Quit\nchoose a number: ")
        valid_option_number = check_option_number(option_number)
        if valid_option_number:
            return option_number
        print("please enter a number from 1 to 3.")


def check_option_number(option_number):
    match_option_number = re.findall('^1|2|3$', option_number)
    if len(match_option_number) == 0:
        return False
    return True


def solve_exercises():
    questions = get_questions()
    with open(r"C:\Users\yarde\PycharmProjects\python\exercises\math_exercises\output.txt", "a") as file:
        for question in questions:
            answer = input(question)
            file.write(answer)


def get_questions():
    questions = []
    with open("input.txt", "r") as file:
        for line in file:
            line.strip()
            questions.append(line)
        return questions

# def check_exercises():
#     with open
#


if __name__ == '__main__':
    main()