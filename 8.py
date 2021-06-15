def compute_grade(the_score):
    if the_score >= 0.9:
        return ("A")
    elif the_score >= 0.8:
        return ("B")
    elif the_score >= 0.7:
        return ("C")
    elif the_score >= 0.6:
        return ("D")
    elif the_score < 0.6:
        return ("F")


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

grade = compute_grade(score)
print(grade)
