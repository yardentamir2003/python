def main():
    people_height = {}
    file = open("input.txt")
    while True:
        for line in file:
            parse_line(line, people_height)
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        age = input("Enter age: ")
        person_info = (first_name, last_name, age)

        if person_info in people_height:
            height = people_height[person_info]
            print("===> The height is ", height)
        else:
            print("===> Sorry, not found")

        answer = input("Do you have another query (yes/no): ")
        if answer == "no":
            break


def parse_line(line, people_height):
    line = line.rstrip()
    word_list = line.split(" ")
    first_name = word_list[0]
    last_name = word_list[1]
    age = word_list[2]
    height = word_list[3]
    tuple_key = (first_name, last_name, age)
    people_height[tuple_key] = height


main()
