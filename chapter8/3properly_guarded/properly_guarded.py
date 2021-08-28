file = open('file.txt')
count = 0
for line in file:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue

    print(words[2])
