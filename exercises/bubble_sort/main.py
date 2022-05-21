def main():
    my_list = [5, 4, 3, 2, 1, 15, 7, 66, 109]
    # for i in range(len(my_list)):
    #     parse_list(my_list)

    parse_number = 0
    while parse_number < len(my_list):
        parse_list(my_list)
        parse_number += 1
    print(my_list)


def parse_list(l):
    index = 0
    while index < len(l) - 1:
        if l[index] > l[index + 1]:
            l[index], l[index + 1] = l[index + 1], l[index]
        index += 1


main()
