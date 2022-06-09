def main():
    numbers_list = []
    while True:
        try:
            number = input("Enter a number: ")
            if number == "done":
                break
            number = float(number)
            numbers_list.append(number)
        except:
            print("Invalid input")
    calculate(numbers_list)


def calculate(numbers_list):
    total = sum(numbers_list)
    length = len(numbers_list)
    minimum = min(numbers_list)
    maximum = max(numbers_list)
    avarage = total / len(numbers_list)
    print("Results are: total: {}, count: {}, average: {}, maximum: {}, minimum: {}".format(total, length, avarage,
                                                                                            maximum, minimum))


main()
