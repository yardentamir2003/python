smallest = None
biggest = None
while True:
    line = input("Enter a number: ")
    if line == 'done':
        break
    try:
        number = float(line)
    except:
        print("Error")
        continue
    if smallest is None or number < smallest:
        smallest = number
    else:
        smallest = smallest
    if biggest is None or number > biggest:
        biggest = number
    else:
        biggest = biggest

print("minimum: ", smallest)
print("maximum: ", biggest)
