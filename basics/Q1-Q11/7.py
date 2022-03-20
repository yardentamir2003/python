def compute_pay(pay_hours, pay_rate):
    if pay_hours < 40:
        pay = float(pay_hours) * float(pay_rate)
        return pay

    else:
        one = 40 * float(pay_rate)
        two = float(pay_hours - 40) * float(pay_rate) * 1.5
        pay = one + two
        return pay


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

payment = compute_pay(hours, rate)
print(payment)

