story = []
while True:
    line = str(input("Enter line: "))

    if line.__contains__("blue"):
        continue

    if line == "quit":
        break

    story.append(line)

for line in story:
    print(line)
