def data_fun(column_name):
    file_input = open("input.csv", "r")
    answers = []
    firstline = True
    for line in file_input:
        if firstline:
            firstline = False
            continue
        if column_name == "first name":
            data = line.split(',')[0]
        elif column_name == "last name":
            data = line.split(',')[1]
        elif column_name == "age":
            data = line.split(',')[2]
        elif column_name == "street number" or "street":
            data = line.split(',')[3]
        elif column_name == "weight":
            data = line.split(',')[4]

        answers.append(data)

    return answers


column_name = input("Enter a column name: ")
data = data_fun(column_name)
for line in data:
    print(line)
