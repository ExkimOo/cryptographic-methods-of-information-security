import re

import numpy as np


class Scytale():
    def encode(self, plaintext, m):
        k = len(plaintext)
        m = self.__is_correct_key(m)
        if m:
            n = (k - 1) // m + 1
            cyphertext = np.array(list(plaintext.ljust(m * n, '*'))).reshape(m, n).T.reshape(-1)
            return ''.join(cyphertext.tolist()).rstrip('*')
        return

    def decode(self, cyphertext, m):
        k = len(cyphertext)
        m = self.__is_correct_key(m)
        if m:
            n = (k - 1) // m + 1
            plaintext = np.array(list(cyphertext.ljust(m*n, '*'))).reshape(n, m).T.reshape(-1)
            return ''.join(plaintext.tolist()).rstrip('*')
        return

    def __is_correct_key(self, m):
        if re.match(r'^[0-9]+$', m):
            return int(m)
        return False

# a = Scytale()
# print(a.encode('hello world', '10'))
# print(a.decode('hlowrd****el ol*****', '10'))
# print(a.decode('НАУАТЮСАТ_К', 3))