def list_creator(file_name):
    num_list = []
    file = open(file_name)
    for line in file:
        line = int(line)
        if line in num_list:
            continue
        else:
            num_list.append(line)
    num_list.sort()
    return num_list


file_name = input("Enter a file name: ")
full_list = list_creator(file_name)
for num in full_list:
    print(num)
