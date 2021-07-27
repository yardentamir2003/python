import re


def palindrome(line):
    line = line.lower()

    new = re.sub('[^a-z]', '', line)
    index = 0
    for index in range(int(len(new) / 2)):
        if new[index] == new[len(new) - index - 1]:
            index = index + 1
            continue
        else:
            return False
            break

    return True


line = str(input("Enter a sentence: "))
answer = palindrome(line)
if answer:
    print("it's a palindrome")

else:
    print("it's not a palindrome")
