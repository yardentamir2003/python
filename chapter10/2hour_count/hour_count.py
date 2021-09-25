def main():
    file = open("input.txt")
    counts = {}
    for line in file:
        if line.startswith("From "):
            line_list = line.split(" ")
            time = line_list[6]
            time_list = time.split(":")
            hour = time_list[0]
            if hour in counts:
                counts[hour] += 1
            else:
                counts[hour] = 1
    list_creator(counts)


def list_creator(counts):
    lst = []
    for key, val in counts.items():
        lst.append((key, val))
    lst.sort()
    for key, val in lst:
        print(key, val)


main()
