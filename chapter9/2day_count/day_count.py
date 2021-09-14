def dictionary_creator(file_name):
    file = open(file_name)
    counts = dict()
    for line in file:
        if line.startswith("From "):
            line = line.split(" ")
            dow = line[2]
            if dow not in counts:
                counts[dow] = 1
            else:
                counts[dow] += 1
    return counts


file_name = input("Enter a file name: ")
counts = dictionary_creator(file_name)
print(counts)
