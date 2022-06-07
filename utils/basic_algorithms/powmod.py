def powmod(a, x, p):
    x_bin_reversed = list(map(int, bin(x)[2:]))[::-1]

    res = 1
    s = a
    for bit in x_bin_reversed:
        if bit:
            res = (res * s) % p
        s = (s * s) % p
    return res
