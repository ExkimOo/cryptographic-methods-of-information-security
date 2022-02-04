import numpy as np

from constants import \
    eng_number_letter_upper, eng_letter_number_upper, \
    rus_letter_number_upper, rus_number_letter_upper, \
    eng_letter_number_lower, eng_number_letter_lower, \
    rus_letter_number_lower, rus_number_letter_lower


class Hill():
    def encode(self, plaintext, key):
        n = np.sqrt(len(key))
        if not n.is_integer():
            print('Длина ключа должна быть равна квадрату натурального числа')
            return

        n = n.astype(np.int64)
        key_matrix = np.array([eng_letter_number_upper[letter] for letter in key]).reshape((n, n))
        if len(plaintext) % n != 0:
            plaintext.join('X'*(len(plaintext) % n))

        cyphertext = []
        for i in range(0, len(plaintext), n):
            letters_vector = np.array([eng_letter_number_upper[letter] for letter in plaintext[i:i + n]])
            result = [eng_number_letter_upper[number] for number in np.dot(key_matrix, letters_vector) % 26]
            cyphertext += result

        return ''.join(cyphertext)

    def decode(self, cyphertext, key):
        n = np.sqrt(len(key))
        if not n.is_integer():
            print('Длина ключа должна быть равна квадрату натурального числа')
            return

        n = n.astype(np.int64)
        key_matrix = np.array([eng_letter_number_upper[letter] for letter in key]).reshape((n, n))
        inv_key_matrix = np.linalg.inv(key_matrix)
        print(inv_key_matrix)


a = Hill()
print(a.encode('CAT', 'GYBNQKURP'))
print(a.decode('FIN', 'GYBNQKURP'))
