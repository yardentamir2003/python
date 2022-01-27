import re


def main():
    formula = input("Enter a formula: ")
    if is_formula_valid(formula):
        print("The formula is valid.")
    else:
        print("The formula is NOT valid.")


def is_formula_valid(formula):
    pattern = '^(-?[a-z]|-?\\.?[0-9]+|-?[0-9]+\\.[0-9]+)\\s*([-+\\/*]\\s*([a-z]|\\-?.?[0-9]+|[0-9]+\\-?.[0-9]+)\\s*)*$'
    checked_formula = re.findall(pattern, formula)
    return len(checked_formula) > 0


if __name__ == '__main__':
    main()
