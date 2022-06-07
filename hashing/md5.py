from bitarray import bitarray
from bitarray.util import int2ba

from constants.constants import ABCD, T, K, S_md5


class MD5:
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
        self.data = [int.from_bytes(self.data[i:i + 32].tobytes(), byteorder='little')
                     for i in range(0, len(self.data), 32)]
        a0, b0, c0, d0 = ABCD
        func_f = lambda x, y, z: (x & y) | (~x & z)
        func_g = lambda x, y, z: (x & z) | (~z & y)
        func_h = lambda x, y, z: x ^ y ^ z
        func_i = lambda x, y, z: y ^ (~z | x)
        modulo = 4294967296

        for _ in range(len(self.data) // 16):
            a, b, c, d = a0, b0, c0, d0
            for n, func in enumerate((func_f, func_g, func_h, func_i)):
                for i in range(16):
                    tmp = func(b, c, d) % modulo
                    tmp = (tmp + self.data[K[n][i % 16]]) % modulo
                    tmp = (tmp + T[16 * n + i]) % modulo
                    tmp = (tmp + a) % modulo
                    tmp = (tmp << S_md5[n][i % 4]) | (tmp >> (32 - S_md5[n][i % 4]))
                    tmp = (tmp + b) % modulo

                    a, b, c, d = d, tmp, b, c

            self.data = self.data[16:]

            a0 = (a + a0) % modulo
            b0 = (b + b0) % modulo
            c0 = (c + c0) % modulo
            d0 = (d + d0) % modulo

        md5_hash = []
        for block in (a0, b0, c0, d0):
            md5_hash += hex(int.from_bytes(int2ba(block, length=32).tobytes(), byteorder='little'))[2:]

        return ''.join(md5_hash)

    def __padding(self):
        length = len(self.data)
        length_bits = bitarray(int2ba(length, 64))
        length_bits = int2ba(int.from_bytes(length_bits.tobytes(), byteorder='little'), 64)
        self.data += bitarray('1') + (448 - 1 - length % 512) * bitarray('0') + length_bits
