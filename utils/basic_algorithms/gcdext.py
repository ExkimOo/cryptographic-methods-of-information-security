def gcdext(a, b):
    if not a:
        return b, 0, 1

    d, x, y = gcdext(b % a, a)
    x, y = y - (b // a) * x, x

    return d, x, y

print(gcdext(130, 253))
