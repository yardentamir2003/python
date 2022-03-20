import re

line = str(input("Enter a sentence: "))
line = line.lower()
line = re.sub('[.,?!]', '', line)
line = line.split(" ")
line = sorted(line)
for word in line:
    print(word)
