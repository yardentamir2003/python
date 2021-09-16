import re


def dictionary_creator(file_name):
    counts = dict()
    file = open(file_name)
    for line in file:
        line = line.lower()
        line = line.rstrip()
        line = re.sub('[.,!?]', "", line)
        words = line.split(" ")
        for word in words:
            if word not in counts:
                counts[word] = 1
            else:
                counts[word] += 1
    return counts


def main():
    file_name = "input.txt"
    counts = dictionary_creator(file_name)
    for pair in counts.items():
        print(pair[0], pair[1])


main()
