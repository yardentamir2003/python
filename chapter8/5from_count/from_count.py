def from_count(file_name):
    file = open(file_name)
    count = 0
    for line in file:
        if line.startswith("From "):
            word_list = line.split(" ")
            print(word_list[1])
            count = count + 1
    return count


file_name = input("Enter a file name: ")
total = from_count(file_name)
print("There were", total, "lines in the file with From as the first word")
