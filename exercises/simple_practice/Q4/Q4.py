def main():
    try:
        hours = float(input("Enter hours: "))
        rate = float(input("Enter rate: "))
        if hours > 40:
            total = pay_more(hours, rate)
        else:
            total = hours * rate
        print("Pay: {}".format(total))
    except:
        print("Please enter numeric input.")


def pay_more(hours, rate):
    standard = 40 * rate
    extra_hours = hours - 40
    extra_pay = extra_hours * rate * 1.5
    total = standard + extra_pay
    return total


main()