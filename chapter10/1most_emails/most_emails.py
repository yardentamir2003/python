def main():
    counts = {}
    file = open("input.txt")
    for line in file:
        if line.startswith("From "):
            words = line.split()
            address = words[1]
            if address not in counts:
                counts[address] = 1
            else:
                counts[address] += 1
    tuple_list(counts)


def tuple_list(counts):
    lst = []
    for key, val in counts.items():
        lst.append((val, key))
    lst.sort(reverse=True)
    item = lst[0]
    print(item[1], ":",  item[0])

main()