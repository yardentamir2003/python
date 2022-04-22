import re


def main():
    while True:
        option_number = get_option_number()
        if option_number == "3":
            break
        if option_number == "1":
            write_answers_file()
        if option_number == "2":
            check_exercises()


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


def write_answers_file():
    answers = solve_exercises()
    with open("output.txt", "w") as file:
        for answer in answers:
            file.write(answer)
            file.write("\n")


def solve_exercises():
    questions = get_questions()
    answers = []
    for question in questions:
        if valid_exercise(question):
            answer = str(eval(question))
        else:
            answer = "wrong exercise"
        answers.append(answer)
    return answers


def get_questions():
    questions = []
    with open("input.txt", "r") as file:
        for line in file:
            line = line.strip()
            questions.append(line)
        return questions


def valid_exercise(exercise):
    match_exercise = re.findall('^[0-9]+[-+*/][0-9]+$', exercise)
    if len(match_exercise) == 0:
        return False
    return True


def check_exercises():
    expected_results = solve_exercises()
    actual_results = get_results("output.txt")
    index = 0
    mistakes = False
    mistakes_number = 0
    wrong_exercises = False
    wrong_exercises_number = 0
    while index < len(actual_results):
        if expected_results[index] == "wrong exercise":
            print("Wrong exercise in line number {}".format(index+1))
            wrong_exercises_number += 1
        elif expected_results[index] != actual_results[index]:
            print("Mistake in line number {}. Should have been {}, but got {}".format(index+1, expected_results[index], actual_results[index]))
            mistakes = True
            mistakes_number += 1
        index += 1
    if mistakes:
        grade = calculate_grade(index, mistakes_number)
    else:
        grade = 100
    if wrong_exercises:
        final_grade = add_factor(grade, wrong_exercises_number, index)
    else:
        final_grade = grade
    print("Your grade is {}".format(final_grade))


def get_results(file_name):
    results = []
    with open(r"C:\Users\yarde\PycharmProjects\python\exercises\math_exercises\{}".format(file_name), "r") as file:
        for line in file:
            line = line.strip()
            results.append(line)
        return results


def calculate_grade(index, mistakes_number):
    line_amount = index
    grade_per_question = 100 / line_amount
    lost_points = mistakes_number * grade_per_question
    grade = 100 - lost_points
    return grade


def add_factor(grade, wrong_exercises_number, index):
    line_amount = index
    grade_per_question = 100 / line_amount
    lost_points = wrong_exercises_number * grade_per_question
    final_grade = grade + lost_points
    return final_grade


if __name__ == '__main__':
    main()
