def double_letter(letter):
    return letter * 2


def split_str(my_str):
    letter_list = list(my_str)
    result = map(double_letter, letter_list)
    result = list(result)
    return "".join(result)


print(split_str("python"))
