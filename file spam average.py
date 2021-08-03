all_numbers = []
file_name = input("Enter a file name: ")
file = open(file_name)

count = 0
for line in file:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence'):
        num = float(line.split(": ")[1])
        all_numbers.append(num)
    count = count + 1

count = int(count)

average = sum(all_numbers) / count
print("Average spam confidence: ", average)
