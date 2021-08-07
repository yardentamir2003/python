def file_split():
    file_input = open("input.txt", "r")
    for line in file_input:
        if line.startswith("name: "):
            line = line.rstrip()
            file_name = line.split(": ")[1]
            file_output = open(file_name, "w")

        elif line.startswith("==="):
            file_output.close()

        else:
            file_output.write(line)


file_split()
