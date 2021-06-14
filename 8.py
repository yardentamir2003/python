score = input("Enter score: ")
try:
    score = float(score)
except:
    print("Bad score")
    exit(1)

if score > 1:
    print("Bad score")
    exit(1)

if score < 0:
    print("Bad score")
    exit(1)

def computegrade(t):
    if t >= 0.9:
        return ("A")
    elif t >= 0.8:
        return ("B")
    elif t >= 0.7:
        return ("C")
    elif t >= 0.6:
        return ("D")
    elif t < 0.6:
        return ("F")

x = computegrade(score)
print(x)

