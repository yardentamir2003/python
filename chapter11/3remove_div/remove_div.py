import re


def main():
    file = open("input.html")
    for line in file:
        line = line.rstrip()
        x = re.findall('^<div>(.+)</div>$', line)
        if len(x) > 0:
            print(x[0])


main()
