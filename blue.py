story = []
while True:
    line = str(input("Enter line: "))

    if "blue" in line:
        continue

    if line == "quit":
        break

    story.append(line)

for line in story:
    print(line)
