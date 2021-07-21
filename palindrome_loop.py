import re
line = str(input("Enter a sentence: "))
line = line.lower()

new = re.sub('[^a-z]', '', line)
for letter in line:
