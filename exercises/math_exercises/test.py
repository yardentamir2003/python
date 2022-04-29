from main import valid_exercise


def test_valid_exercise():
    valid = valid_exercise("1+2+6")
    if valid_exercise:
        print("should be not valid.")

    valid = valid_exercise("309-80")
    if not valid:
        print("should be valid")


test_valid_exercise()