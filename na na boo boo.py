file_name = input("Enter a file name: ")
if file_name == "na na boo boo":
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
    exit(1)
try:
    file = open(file_name)
except:
    print('File cannot be opened:', file_name)
    exit(1)

count = 0
for line in file:
    line = line.rstrip()
    if line.startswith('Subject'):
        count = count + 1

print("There were", count, "subject lines in", file_name)
