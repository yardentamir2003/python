def main():
    file = open("input.txt")
    counts = {}
    for line in file:
        if line.startswith("From "):
            line = line.split(" ")
            mail = line[1]
            if mail in counts:
                counts[mail] += 1
            else:
                counts[mail] = 1
    tuple_list(counts)


def tuple_list(counts):
    lst = []
    for key, val in counts.items():
        lst.append((val, key))
    lst.sort(reverse=True)
    item = lst[0]
    print(item[1], item[0])


main()
