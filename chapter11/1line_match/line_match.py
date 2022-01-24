import re


def main():
    regular_expression = input("Enter a regular expression: ")
    file = open("input.txt")
    count = 0
    for line in file:
        line = line.rstrip()
        if re.search(regular_expression, line):
            count += 1
    print("input.txt had", count, "lines that matched", regular_expression)

main()