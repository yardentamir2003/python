def dictionary_creator(file_name):
    file = open(file_name)
    counts = dict()
    for line in file:
        if line.startswith("From "):
            line = line.split(" ")
            mail = line[1]
            if mail not in counts:
                counts[mail] = 1
            else:
                counts[mail] += 1
    return counts


file_name = input("Enter a file name: ")
counts = dictionary_creator(file_name)
print(counts)