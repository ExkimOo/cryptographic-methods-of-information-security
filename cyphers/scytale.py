import numpy as np


class Scytale():
    def encode(self, plaintext, m):
        k = len(plaintext)
        n = (k - 1) // m + 1
        cyphertext = np.array(list(plaintext.ljust(m * n, '*'))).reshape(m, n).T.reshape(-1)
        return ''.join(cyphertext.tolist())

    def decode(self, cyphertext, m):
        k = len(cyphertext)
        n = (k - 1) // m + 1
        plaintext = np.array(list(cyphertext.ljust(m*n, '*'))).reshape(n, m).T.reshape(-1)
        return ''.join(plaintext.tolist())


# a = Scytale()
# print(a.encode('нас атакуют', 3))
# # print(a.decode('РНОАЫЙКЕСЕ_КТВА', 3))
# print(a.decode('НАУАТЮСАТ_К', 3))