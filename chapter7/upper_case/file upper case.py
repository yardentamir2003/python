file_name = "C:\\Users\\yarde\\Downloads\\mbox-short.txt"
file_name = "../spam_average/a.txt"

file_name = input("Enter a file name: ")
file = open(file_name)

for line in file:
    line = line.upper()
    line = line.rstrip()
    print(line)
