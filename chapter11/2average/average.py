import re


def main():
    file = open("input.txt")
    sum = 0
    count = 0
    for line in file:
        line = line.rstrip()
        x = re.findall('^New Revision: ([0-9]+)', line)
        if len(x) > 0:
            x = int(x[0])
            sum = sum + x
            count += 1
    avarage = int(sum / count)
    print("avarage:", avarage)


main()
