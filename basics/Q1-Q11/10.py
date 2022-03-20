total = 0
count = 0
while True:
    line = input("Enter a number: ")
    if line == 'done':
        break
    number = 0
    try:
        number = float(line)
    except:
        print("Error")
        continue
    total = total + number
    count = count + 1

if total == 0:
    print("total, count, average = 0")
else:
    print("total: ", total)
print("count: ", count)
print("average: ", total / count)
