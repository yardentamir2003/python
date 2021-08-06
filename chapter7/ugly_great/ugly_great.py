def change_file():
    file_input = open("input.txt", "rt")
    file_output = open("output.txt", "wt")
    for line in file_input:
        replaced_line = replace_ugly(line)
        file_output.write(replaced_line)

    file_output.close()
    file_input.close()


def replace_ugly(input_string):
    output_string = input_string.replace(" ugly", " great")
    return output_string


change_file()
