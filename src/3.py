hours = input("Enter hours: ")
try:
    hours = float(hours)
except:
    print("Please enter numeric input")
    exit(1)
rate = input("Enter rate: ")
try:
    rate = float(rate)
except:
    print("Please enter numeric input")
    exit(1)





if hours < 40:
    print("pay: ", float(hours) * float(rate))

else:
    one = 40 * float(rate)
    two = float(hours - 40) * float(rate) * 1.5
    print("pay: ", one + two)
