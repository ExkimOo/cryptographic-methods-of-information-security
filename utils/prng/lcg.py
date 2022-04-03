seed = 1


def lcg(rand_max=256):
    global seed
    a = 1664525
    c = 1013904223
    m = 2 ** 32

    seed = ((a * seed + c) % m)

    return seed % rand_max


def set_seed(s):
    global seed
    seed = s