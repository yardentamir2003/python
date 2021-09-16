def list_creator(file_name):
    unique_words = []
    file = open(file_name)
    for line in file:
        line = line.lower()
        line = line.rstrip()
        word_list = line.split(" ")
        for word in word_list:
            if word in unique_words:
                continue
            else:
                unique_words.append(word)
    return unique_words


def file_sorter():
    file_name = input("Enter a file name: ")
    full_list = list_creator(file_name)
    full_list.sort()
    print(full_list)


file_sorter()
