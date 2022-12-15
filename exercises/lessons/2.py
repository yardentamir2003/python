while True:
    number = input("Enter a number between 10 to 99: ")
    if 10 <= int(number) <= 99:
        break
    else:
        print("Error, please enter a valid number.")

left_number = int(number[0])
right_number = int(number[1])

new_left_number = left_number + 2
new_right_number = right_number + 2

if new_right_number >= 10:
    number1 = str(new_right_number)[0]
    number2 = str(new_right_number)[1]
    new_right_number = int(number1) + int(number2)

if new_left_number >= 10:
    number1 = str(new_left_number)[0]
    number2 = str(new_left_number)[1]
    new_left_number = int(number1) + int(number2)

final_number = new_left_number * 10 + new_right_number
print(final_number)
