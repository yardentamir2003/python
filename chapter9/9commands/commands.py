def main():
    file = open("input.txt")
    word_dictionary = {}
    for line in file:
        dictionary_creator(line, word_dictionary)
    for key in word_dictionary:
        if word_dictionary[key] != 0:
            print(key, word_dictionary[key])
        else:
            continue


def dictionary_creator(line, word_dictionary):
    line = line.rstrip()
    if line.startswith("ADD"):
        words = line.split(" ")
        word = words[1]
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1
    elif line.startswith("REMOVE"):
        words = line.split(" ")
        word = words[1]
        word_dictionary[word] -= 1


main()
