line = str(input("Enter a sentence: "))

while "duplicate" in line:
    duplicate_begin = line.find("duplicate")
    duplicate_end = line.find(' ', duplicate_begin)
    times = line[duplicate_end + 1: duplicate_end + 2]
    times = int(times)
    end_word = line.find(' ', duplicate_end + 3)
    end_word = int(end_word)
    if end_word == -1:
        new_string = line[0:duplicate_begin] + (line[duplicate_end + 3:] + (' ')) * times
        line = new_string
    else:
        new_string = line[0:duplicate_begin] + line[duplicate_end + 3:end_word + 1] * times + line[end_word + 1:]
        line = new_string

print(line)