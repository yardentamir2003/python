import random

low = input("Enter low: ")
high = input("Enter high: ")
threshold = input("Enter threshold: ")


def run_casino(a, b, c):
    t = [a, b]
    x = random.choice(t)
    print(x)

    if x > c:
        print("You win")
    else:
        print("You loose")


run_casino(low, high, threshold)
