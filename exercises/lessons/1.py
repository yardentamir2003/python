n = input("Enter a number: ")
numbers_list = []
result = ""
for number in range(1, int(n) + 1):
    numbers_list.append(number)
    if number == int(n):
        result = result + str(number) + "="
    else:
        result = result + str(number) + "+"
print(result + str(sum(numbers_list)))

n1 = int(input("Enter number one: "))
n2 = int(input("Enter number two: "))
n3 = int(input("Enter number three: "))
numbers_list = [n1, n2, n3]
numbers_list.sort()
print(numbers_list)
for number in numbers_list:
    print(number)
if sum(numbers_list) > 100:
    print("More than 100, ", str(sum(numbers_list)))
else:
    print("Less than 100,", str(sum(numbers_list)))
