import re


def find_index(word, word_list):
    index = 0
    while index < len(word_list):
        if word == word_list[index]:
            break
        else:
            index = index + 1

    return index


def lists_creator(word_list, count_list, line):
    words = line.split(" ")

    for word in words:
        if word in word_list:
            index = find_index(word, word_list)
            count_list[index] = count_list[index] + 1

        else:
            word_list.append(word)
            count_list.append(1)


def story_count(file_name):
    word_list = []
    count_list = []
    file = open(file_name)
    for line in file:
        line = line.lower()
        line = line.rstrip()
        line = re.sub('[.,!?]', "", line)
        lists_creator(word_list, count_list, line)
    return word_list, count_list


def main():
    file_name = "input.txt"
    word_list, count_list = story_count(file_name)
    for i in range(len(word_list)):
        print(word_list[i], end=" ")
        print(count_list[i])


main()
