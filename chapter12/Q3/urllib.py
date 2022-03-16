import urllib.request, urllib.parse, urllib.error

URL = input("Enter URL:")
file = urllib.request.urlopen(URL)
characters_count = 0
limit = 1000
enter_here = True
for line in file:
    characters_count += len(line)
    if characters_count < 1000:
        print(line.decode().strip())
    else:
        if enter_here:
            dont_print = characters_count - limit
            print(line[:-dont_print].decode(), end='')
            enter_here = False
print("\ncharacters count = ", characters_count)




