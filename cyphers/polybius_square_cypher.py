import numpy as np

import re

from widgets.constants import RUS_LETTERS, ENG_LETTERS


class PolybiusSquare():
    def __init__(self):
        self.eng_polybius_square = np.array(list(ENG_LETTERS.translate({ord('J'): None}))).reshape((5, 5))
        self.rus_polybius_square = np.array(list(RUS_LETTERS.translate({ord(i): None for i in 'ЁЗЙСЪЩЭХ'}))).reshape(
            (5, 5))

    def encode(self, plaintext, method='1'):
        cyphertext = []
        plaintext = plaintext.upper()
        if method == '1':
            for letter in self.__remove_letters(plaintext):
                result = np.array(letter)
                if np.isin(letter, self.eng_polybius_square):
                    (i, j) = np.where(self.eng_polybius_square == letter)
                    result = self.eng_polybius_square[(i + 1) % 5, j]
                elif np.isin(letter, self.rus_polybius_square):
                    (i, j) = np.where(self.rus_polybius_square == letter)
                    result = self.rus_polybius_square[(i + 1) % 5, j]
                cyphertext += result.tolist()
        elif method == '2' or method == '3':
            if re.match(r'^[A-Za-z]+$', plaintext):
                polybius_square = self.eng_polybius_square
            elif re.match(r'^[А-Яа-я]+$', plaintext):
                polybius_square = self.rus_polybius_square
            else:
                return

            h_indexes = []
            v_indexes = []
            for letter in plaintext:
                (i, j) = map(lambda x: int(x), np.where(polybius_square == letter))
                h_indexes.append(i)
                v_indexes.append(j)

            indexes = v_indexes + h_indexes
            if method == '3':
                indexes = indexes[1:] + indexes[:1]

            for i in range(0, len(indexes), 2):
                cyphertext += polybius_square[indexes[i + 1], indexes[i]]

        return ''.join(cyphertext)

    def decode(self, cyphertext, method='1'):
        plaintext = []
        cyphertext = cyphertext.upper()
        if method == '1':
            for letter in self.__remove_letters(cyphertext):
                result = np.array(letter)
                if np.isin(letter, self.eng_polybius_square):
                    (i, j) = np.where(self.eng_polybius_square == letter)
                    result = self.eng_polybius_square[(i - 1) % 5, j]
                elif np.isin(letter, self.rus_polybius_square):
                    (i, j) = np.where(self.rus_polybius_square == letter)
                    result = self.rus_polybius_square[(i - 1) % 5, j]
                plaintext += result.tolist()
        elif method == '2' or method == '3':
            if re.match(r'^[A-Za-z]+$', cyphertext):
                polybius_square = self.eng_polybius_square
            elif re.match(r'^[А-Яа-я]+$', cyphertext):
                polybius_square = self.rus_polybius_square
            else:
                return

            indexes = []
            for letter in cyphertext:
                (i, j) = map(lambda x: int(x), np.where(polybius_square == letter))
                indexes.append(i)
                indexes.append(j)

            for i in range(0, len(indexes), 2):
                indexes[i], indexes[i + 1] = indexes[i + 1], indexes[i]
            if method == '3':
                indexes = indexes[-1:] + indexes[:-1]

            h_indexes = indexes[len(indexes)//2:]
            v_indexes = indexes[:len(indexes)//2]

            plaintext = []
            for i, j in zip(h_indexes, v_indexes):
                plaintext.append(polybius_square[i, j])

        plaintext = ''.join(plaintext)
        dual_letters = 'IЕЖИРШЬ'
        possible_letters = 'JЭЗЙСЩЪ'
        for i in range(len(dual_letters)):
            plaintext = plaintext.replace(dual_letters[i], '(' + dual_letters[i] + '|' + possible_letters[i] + ')', -1)

        return plaintext

    def __remove_letters(self, text):
        return text.translate({ord(letter_fr): letter_to for letter_fr, letter_to in zip('JЁЭЗЙСЩЪ', 'IЕЕЖИРШЬ')})


# a = PolybiusSquare()
# print(a.encode('SOMETEXT', '2'))
# print(a.encode('SOMETEXT', '3'))
# print(a.decode('SWYSOCDU', '2'))
# print(a.decode('IUPTNQVO', '3'))
