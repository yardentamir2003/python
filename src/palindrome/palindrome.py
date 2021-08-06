import re
line = str(input("Enter a sentence: "))
line = line.lower()

new = re.sub('[^a-z]', '', line)
if new == new[::-1]:
    print("it's a palindrome")
else:
    print("it's not a palindrome")
