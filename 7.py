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

def computepay(a, b):
    if a < 40:
        pay = float(a) * float(b)
        return pay

    else:
        one = 40 * float(b)
        two = float(a - 40) * float(b) * 1.5
        pay = one + two
        return pay

x = computepay(hours, rate)
print(x)
