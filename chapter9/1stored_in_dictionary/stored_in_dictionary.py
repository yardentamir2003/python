file = open("words.txt")
dictionary = dict()
lines_list = []
for line in file:
    line = line.rstrip()
    lines_list.append(line)
for line in lines_list:
    word_list = line.split(" ")
    for word in word_list:
        dictionary[word] = ""


