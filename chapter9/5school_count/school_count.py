def main():
    file_name = input("Enter a file name: ")
    counts = dictionary_creator(file_name)
    print(counts)


def dictionary_creator(file_name):
    file = open(file_name)
    counts = dict()
    for line in file:
        if line.startswith("From "):
            line = line.split(" ")
            email = line[1]
            index = find_index(email)
            school = email[index + 1:]
            if school not in counts:
                counts[school] = 1
            else:
                counts[school] += 1
    return counts


def find_index(email):
    index = 0
    for character in email:
        if character != "@":
            index = index + 1
        else:
            return index


main()
