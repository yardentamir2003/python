import re

line = str(input("Enter a sentence: "))
line = line.lower()

new = re.sub('[^a-z]', '', line)
index = 0
for index in range(int(len(new) / 2)):
    if new[index] == new[len(new) - index - 1]:
        index = index + 1
        continue
    else:
        print("it's not a palindrome.")
        exit(1)

print("it's a palindrome.")
