# def duplicate(letter):
#     return letter * 2


def double_letter(my_str):
    # return "".join(list(map(duplicate, list(my_str))))
    return "".join(list(map(lambda letter: letter*2, list(my_str))))


print(double_letter("python"))
