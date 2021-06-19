import random


def run_casino(high_number, low_number, threshold_number):
    high_number = int(high_number)
    low_number = int(low_number)
    threshold_number = int(threshold_number)
    x = random.randint(high_number, low_number)
    print(x)

    if x > threshold_number:
        print("You win")
    else:
        print("You loose")


low = input("Enter low: ")
high = input("Enter high: ")
threshold = input("Enter threshold: ")

run_casino(low, high, threshold)
run_casino(low, high, threshold)
run_casino(low, high, threshold)
