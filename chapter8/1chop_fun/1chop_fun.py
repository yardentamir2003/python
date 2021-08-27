def chop(t):
    del t[0]
    del t[len(t) - 1]


def middle(t):
    return t[1:(len(t) - 1)]


letters = ['a', 'b', 'c']
new = middle(letters)
print(letters)
print(new)

new = chop(letters)
print(letters)
print(new)
