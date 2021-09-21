def main():
    word_dictionary = {}
    file = open("input.txt")
    for line in file:
        line = line.rstrip()
        parse_line(line, word_dictionary)
    for key, value in word_dictionary.items():
        print(key, value)


def parse_line(line, word_dictionary):
    words = line.split(" ")
    for word in words:
        parse_word(word, word_dictionary)


def parse_word(word, word_dictionary):
    for i in range(len(word)):
        prefix = word[:i + 1]
        if prefix in word_dictionary:
            word_dictionary[prefix] += 1
        else:
            word_dictionary[prefix] = 1


main()
