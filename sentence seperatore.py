line = str(input("Enter a sentence: "))
line = line.lower()
import re
line = re.sub('[.,?!]', '', line)
line = line.split(" ")
index = (len(line) - 1)
while index >= 0:
    word = line[index]
    print(word)
    index = index - 1
