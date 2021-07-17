line = str(input("Enter a sentence: "))
duplicate_begin = line.find("duplicate")
print(duplicate_begin)
duplicate_end = line.find(' ',duplicate_begin)
print(duplicate_end)
times = line[duplicate_end: duplicate_end+2]
times = int(times)
new_string = line[0:duplicate_begin] + line[duplicate_end+3:]
print(new_string)

