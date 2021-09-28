def main():
    d = {}
    file = open("input.txt")
    parse_line(file, d)
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    age = input("Enter age: ")
    t = (first_name, last_name, age)
    try:
        height = d[t]
        print("===> The height is ", height)
    except:
        print("===> Sorry, not found")
    answer = input("Do you have another query (yes/no): ")
    yes_no(answer)


def parse_line(file, d):
    for line in file:
        line = line.rstrip()
        word_list = line.split(" ")
        first_name = word_list[0]
        last_name = word_list[1]
        age = word_list[2]
        height = word_list[3]
        tuple_key = (first_name, last_name, age)
        d[tuple_key] = height


def yes_no(answer):
    if answer == "yes":
        main()


main()

# a = (1, 2)
# d = {}
# d[a] = 9
