def dupli(line):
    duplicate_begin = line.find("duplicate")
    duplicate_end = line.find(' ', duplicate_begin)
    times_begin = duplicate_end + 1
    times_end = line.find(" ", duplicate_end + 1)
    times = line[times_begin:times_end]
    times = int(times)
    end_word = line.find(' ', times_end + 1)
    end_word = int(end_word)
    if end_word == -1:
        new_string = line[0:duplicate_begin] + (line[times_end + 1:] + ' ') * times
        line = new_string
    else:
        new_string = line[0:duplicate_begin] + line[times_end + 1:end_word + 1] * times + line[end_word + 1:]
        line = new_string

    return line


line = str(input("Enter a sentence: "))

while "duplicate" in line:
    line = dupli(line)
    print(line)


