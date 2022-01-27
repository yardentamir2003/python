import re


def main():
    file = open("input.html")
    for line in file:
        line = line.rstrip()
        div_line = re.findall('<div>(.+?)</div>', line)
        if len(div_line) > 0:
            for item in div_line:
                print(item)


main()
