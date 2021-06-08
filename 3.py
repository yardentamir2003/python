hours = input("Enter hours: ")
rate = input("Enter rate: ")
try:
    hours = float(hours)
    rate = float(rate)
    if hours < 40:
        print("pay: ", float(hours) * float(rate))

    else:
        one = int(40) * float(rate)
        two = float(hours - 40) * float(rate) * 1.5
    print("pay: ", int(one + two))

except:
       print("Please enter numeric input")
