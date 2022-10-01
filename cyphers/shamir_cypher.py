from random import randint

from utils.basic_algorithms.gcdext import gcdext
from utils.basic_algorithms.gcd import gcd
from utils.basic_algorithms.powmod import powmod


def generate_c_d(prime):
    while True:
        c = randint(prime // 2, prime - 2)
        if gcd(c, prime - 1) == 1:
            _, d, _ = gcdext(c, prime - 1)
            while d < 0:
                d += prime - 1

            return c, d

def send_message(message, p, ca, da, cb, db, file_in='', file_out=''):
    result = []

    if file_in:
        with open(file_in, 'rb') as file_input, \
                open(file_out, 'wb+') as file_output:
            data = file_input.read()

            for symbol in data:
                block_1 = powmod(symbol, ca, p)
                block_2 = powmod(block_1, cb, p)
                block_3 = powmod(block_2, da, p)
                block_4 = powmod(block_3, db, p)
                result.append(int.to_bytes(block_4, length=1, byteorder='little'))

            file_output.write(b''.join(result))
    else:
        for symbol in message:
            encrypted_block_1 = powmod(ord(symbol), ca, p)
            encrypted_block_2 = powmod(encrypted_block_1, cb, p)
            encrypted_block_3 = powmod(encrypted_block_2, da, p)
            encrypted_block_4 = powmod(encrypted_block_3, db, p)
            result.append(chr(encrypted_block_4))

        return ''.join(result)

# print(send_message('123', 97, 5, 77, 7, 55))