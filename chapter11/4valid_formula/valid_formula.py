import re


def main():
    formula = input("Enter a formula: ")
    x = check_formula(formula)
    if len(x) > 0:
        print("The formula is valid.")
    else:
        print("The formula is NOT valid.")


def check_formula(formula):
    checked_formula = re.findall('^([a-z]|-?\.?[0-9]+|-?[0-9]+\.[0-9]+)\s*([-+\/*]\s*([a-z]|\.?[0-9]+|[0-9]+\.[0-9]+)\s*)*$', formula)
    return checked_formula


main()
