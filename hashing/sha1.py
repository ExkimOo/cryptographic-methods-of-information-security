from bitarray import bitarray
from bitarray.util import int2ba

from constants.constants import ABCDE


class SHA1:
    def __init__(self, data, type='text'):
        self.data = bitarray()
        match type:
            case 'text':
                self.data.frombytes(data.encode('utf-8'))
            case 'file':
                with open(data, 'rb') as file:
                    self.data.fromfile(file)

    def generate_hash(self):
        self.__padding()
        self.data = [int.from_bytes(self.data[i:i + 32].tobytes(), byteorder='big')
                     for i in range(0, len(self.data), 32)]
        a0, b0, c0, d0, e0 = ABCDE
        func_1 = lambda x, y, z: (x & y) | (~x & z)
        func_2 = lambda x, y, z: x ^ y ^ z
        func_3 = lambda x, y, z: (x & y) | (x & z) | (y & z)
        modulo = 4294967296

        for _ in range(len(self.data) // 16):
            a, b, c, d, e = a0, b0, c0, d0, e0

            w = self.data[:16]
            w += [None] * 64
            for i in range(16, 80):
                w[i] = (((w[i - 3] ^ w[i - 8] ^ w[i - 14] ^ w[i - 16]) << 1) |
                        ((w[i - 3] ^ w[i - 8] ^ w[i - 14] ^ w[i - 16]) >> 31)) % modulo

            for n, (func, k) in enumerate(((func_1, 0x5A827999),
                                           (func_2, 0x6ED9EBA1),
                                           (func_3, 0x8F1BBCDC),
                                           (func_2, 0xCA62C1D6))):
                for i in range(20):
                    tmp = func(b, c, d)
                    tmp = (tmp + ((a << 5) | (a >> 27))) % modulo
                    tmp = (tmp + e) % modulo
                    tmp = (tmp + k) % modulo
                    tmp = (tmp + w[n * 20 + i]) % modulo

                    a, b, c, d, e = tmp, a, (b << 30) | (b >> 2), c, d

            self.data = self.data[16:]

            a0 = (a + a0) % modulo
            b0 = (b + b0) % modulo
            c0 = (c + c0) % modulo
            d0 = (d + d0) % modulo
            e0 = (e + e0) % modulo

        sha1_hash = []
        for block in (a0, b0, c0, d0, e0):
            sha1_hash += hex(int.from_bytes(int2ba(block, length=32).tobytes(), byteorder='big'))[2:]

        return ''.join(sha1_hash)

    def __padding(self):
        length = len(self.data)
        length_bits = bitarray(int2ba(length, 64))
        self.data += bitarray('1') + (448 - 1 - length % 512) * bitarray('0') + length_bits
