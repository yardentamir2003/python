from main import valid_exercise, get_questions


def test_valid_exercise():
    valid = valid_exercise("1+2+6")
    if valid:
        print("should be not valid.")

    valid = valid_exercise("309-80")
    if not valid:
        print("should be valid")

    print("test ok")


def test_get_questions():
    questions = get_questions("test_questions.txt")
    expected = ['2+4', '6*6']
    if expected != questions:
        print('test failed')


test_valid_exercise()

test_get_questions()
