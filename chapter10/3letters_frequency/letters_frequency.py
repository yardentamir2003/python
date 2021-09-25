import re


def main():
    letters_dictionary = {}
    file = open("song_lyrics")
    for line in file:
        line = line.rstrip()
        line = line.lower()
        line = re.sub('[^a-z]', '', line)
        word_list = line.split(" ")
        parse_line(word_list, letters_dictionary)
    list_creator(letters_dictionary)


def parse_line(word_list, letters_dictionary):
    for word in word_list:
        for letter in word:
            if letter in letters_dictionary:
                letters_dictionary[letter] += 1
            else:
                letters_dictionary[letter] = 1


def list_creator(letters_dictionary):
    letter_list = []
    for key, val in letters_dictionary.items():
        letter_list.append((val, key))
    letter_list.sort(reverse=True)
    for key, val in letter_list:
        print(val, key)


main()