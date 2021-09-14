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


def main():
    file_name = input("Enter a file name: ")
    counts = dictionary_creator(file_name)
    values = counts.values()
    max_value = max(values)
    key_list = list(counts.keys())
    val_list = list(counts.values())
    position = val_list.index(max_value)
    print(key_list[position], max_value)


main()