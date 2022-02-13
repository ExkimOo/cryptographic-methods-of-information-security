import re

import numpy as np

from widgets.constants import ENG_LETTERS, RUS_LETTERS

ENG_LETTERS += ' .?'
RUS_LETTERS += ' .?!'

class Hill():
    def __init__(self, key, lang):
        self.key = key
        self.lang = lang
        if self.lang == 'ENG':
            self.LETTERS = ENG_LETTERS
        else:
            self.LETTERS = RUS_LETTERS
        self.modulo = len(self.LETTERS)

    def encode(self, plaintext):
        n = self.__is_correct_key()
        if not n:
            return

        cyphertext = []
        if self.__is_correct_text(plaintext):
            n = n.astype(np.int64)
            key_matrix = np.array([self.LETTERS.index(letter) for letter in self.key]).reshape((n, n))
            if len(plaintext) % n != 0:
                plaintext += ' '*(n - len(plaintext) % n)

            for i in range(0, len(plaintext), n):
                numbers_vector = np.array([self.LETTERS.index(letter) for letter in plaintext[i:i + n]])
                result = [self.LETTERS[number] for number in np.dot(key_matrix, numbers_vector) % self.modulo]
                cyphertext += result

        return ''.join(cyphertext)

    def decode(self, cyphertext):
        n = self.__is_correct_key()
        if not n:
            return

        plaintext = []
        if self.__is_correct_text(cyphertext):
            n = n.astype(np.int64)
            key_matrix = np.array([self.LETTERS.index(letter) for letter in self.key]).reshape((n, n))
            inv_key_matrix = self.__invert_matrix(key_matrix)

            if not np.all(inv_key_matrix):
                print(inv_key_matrix)
                print('Матрица является вырожденной, декодирование невозможно')
                return

            if len(cyphertext) % n != 0:
                cyphertext += ' '*(n - len(cyphertext) % n)

            for i in range(0, len(cyphertext), n):
                numbers_vector = np.array([self.LETTERS.index(letter) for letter in cyphertext[i:i + n]])
                result = [self.LETTERS[number] for number in np.dot(inv_key_matrix, numbers_vector) % self.modulo]
                plaintext += result

        return ''.join(plaintext)

    def __invert_matrix(self, key_matrix):
        n = key_matrix.shape[0]

        det = np.linalg.det(key_matrix) % self.modulo
        det = det.astype(np.int64)
        _, inversed_det, _ = self.__gcdext(det, self.modulo)

        adjunct_matrix = np.empty((n, n), dtype=np.int64)

        for i in range(n):
            for j in range(n):
                matrix = np.delete(key_matrix, i, axis=0)
                matrix = np.delete(matrix, j, axis=1)
                minor = np.round(np.linalg.det(matrix) % self.modulo)
                adjunct_matrix[j, i] = ((-1)**(i + j)*minor) % self.modulo

        return (adjunct_matrix * inversed_det) % self.modulo

    def __gcdext(self, num1, num2):
        if num1 == 0:
            return (num2, 0, 1)
        else:
            div, x, y = self.__gcdext(num2 % num1, num1)
        return (div, y - (num2 // num1) * x, x)

    def __is_correct_key(self):
        n = np.sqrt(len(self.key))
        if not n.is_integer():
            print('Длина ключа должна быть равна квадрату натурального числа')
            return

        if self.lang == 'ENG' and re.match(r'^[A-Z .?]+$', self.key):
            return np.round(n)
        elif self.lang == 'RUS' and re.match(r'^[А-Я .?!]+$', self.key):
            return np.round(n)
        else:
            print('Неправильный ключ')
            return

    def __is_correct_text(self, text):
        if self.lang == 'ENG' and re.match(r'^[A-Z .?]+$', text):
            return True
        elif self.lang == 'RUS' and re.match(r'^[А-Я .?!]+$', text):
            return True
        else:
            print('Неправильный текст')
            return

# a = Hill('HELL', 'ENG')
# print(a.encode('ABCD EFGH IJKL.'))
# print(a.decode('EL  YLBFIPFN.?DD'))

