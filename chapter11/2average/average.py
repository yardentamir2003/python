import re


def main():
    file = open("input.txt")
    revision_sum = 0
    count = 0
    for line in file:
        line = line.rstrip()
        revision_number = re.findall('^New Revision: ([0-9]+)', line)
        if len(revision_number) > 0:
            revision_number = int(revision_number[0])
            revision_sum = revision_sum + revision_number
            count += 1
    average = int(revision_sum / count)
    print("average:", average)


main()
