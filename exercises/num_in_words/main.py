number2word = {0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
               6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
               11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
               15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen',
               19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty',
               50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty',
               90: 'Ninety'}


def main():
    number = input("Enter number: ")
    words = return_answer(number)
    print(words)


def return_answer(number):
    try:
        number = int(number)
    except:
        words = "Error please enter a number up to 10000."
        return words

    if number <= 20:
        words = less_than_20(number)
    elif 20 < number <= 99:
        words = two_digits(number)
    elif 100 <= number <= 999:
        words = three_digits(number)
    elif 1000 <= number <= 9999:
        words = four_digits(number)
    elif number == 10000:
        words = "Ten thousands"
    else:
        words = "Error please enter a number up to 10000."

    return words


def less_than_20(number):
    word = number2word.get(number)
    return word


def two_digits(number):
    tens_digit = str(number)[0]
    tens = int(tens_digit) * 10
    tens = number2word.get(int(tens))
    unit_digit = str(number)[1]
    word = number2word.get(int(unit_digit))
    if word == "Zero" and tens == "Zero":
        return ""
    if unit_digit == "0":
        return tens
    if tens == "Zero":
        return word

    answer = "{} {}".format(tens, word)
    return answer


def three_digits(number):
    hundreds = str(number)[0]
    hundreds = number2word.get(int(hundreds))
    tens = str(number)[1:]
    tens = two_digits(tens)
    if hundreds == "Zero":
        return tens
    else:
        if hundreds == "One":
            words = "{} hundred {}".format(hundreds, tens)
        else:
            words = "{} hundreds {}".format(hundreds, tens)
        return words


def four_digits(number):
    thousands = str(number)[0]
    thousands = number2word.get(int(thousands))
    hundreds = str(number)[1:]
    hundreds = three_digits(hundreds)
    if thousands == "One":
        words = "{} thousand {}".format(thousands, hundreds)
    else:
        words = "{} thousands {}".format(thousands, hundreds)
    return words


if __name__ == '__main__':
    main()
