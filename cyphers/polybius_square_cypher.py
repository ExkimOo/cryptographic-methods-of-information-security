import re

import numpy as np

from constants.constants import RUS_LETTERS, ENG_LETTERS


class PolybiusSquare():
    def __init__(self, lang='ENG'):
        self.eng_polybius_square = np.array(list(ENG_LETTERS.translate({ord('J'): None}))).reshape((5, 5))
        self.rus_polybius_square = np.array(list(RUS_LETTERS.translate({ord(i): None for i in 'ЁЗЙСЪЩЭХ'}))).reshape(
            (5, 5))
        self.lang = lang

    def encode(self, plaintext, method='1'):
        cyphertext = []
        plaintext = plaintext.upper()
        if method == '1':
            cyphertext = self.__first_method(plaintext, 'enc')
        elif method == '2' or method == '3':
            plaintext = self.__remove_letters(plaintext)

            if self.lang == 'ENG':
                polybius_square = self.eng_polybius_square
                insert_indexes = [(m.start(0), m.end(0)) for m in re.finditer(r'[A-Za-z]+', plaintext)]
                tokens = [plaintext[start:end] for start, end in insert_indexes]
            else:
                polybius_square = self.rus_polybius_square
                insert_indexes = [(m.start(0), m.end(0)) for m in re.finditer(r'[А-Яа-яЁё]+', plaintext)]
                tokens = [plaintext[start:end] for start, end in insert_indexes]

            plaintext_cleaned = ''.join(tokens)

            h_indexes = []
            v_indexes = []
            for letter in plaintext_cleaned:
                (i, j) = map(lambda x: int(x), np.where(polybius_square == letter))
                h_indexes.append(i)
                v_indexes.append(j)

            indexes = v_indexes + h_indexes
            if method == '3':
                indexes = indexes[1:] + indexes[:1]

            for i in range(0, len(indexes), 2):
                cyphertext += polybius_square[indexes[i + 1], indexes[i]]

            return self.__insert_encoded_text(plaintext, cyphertext, insert_indexes)

        return cyphertext

    def decode(self, cyphertext, method='1'):
        plaintext = []
        cyphertext = cyphertext.upper()
        if method == '1':
            plaintext = self.__first_method(cyphertext, 'dec')
        elif method == '2' or method == '3':
            cyphertext = self.__remove_letters(cyphertext)

            if self.lang == 'ENG':
                polybius_square = self.eng_polybius_square
                insert_indexes = [(m.start(0), m.end(0)) for m in re.finditer(r'[A-Za-z]+', cyphertext)]
                tokens = [cyphertext[start:end] for start, end in insert_indexes]
            else:
                polybius_square = self.rus_polybius_square
                insert_indexes = [(m.start(0), m.end(0)) for m in re.finditer(r'[А-Яа-яЁё]+', cyphertext)]
                tokens = [cyphertext[start:end] for start, end in insert_indexes]

            cyphertext_cleaned = ''.join(tokens)

            indexes = []
            for letter in cyphertext_cleaned:
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

            plaintext = self.__insert_encoded_text(cyphertext, plaintext, insert_indexes)

        if self.lang == 'ENG':
            dual_letters = 'I'
            possible_letters = 'J'
        else:
            dual_letters = 'ЕЖИРШЬ'
            possible_letters = 'ЭЗЙСЩЪ'

        for i in range(len(dual_letters)):
            plaintext = plaintext.replace(dual_letters[i], '(' + dual_letters[i] + '|' + possible_letters[i] + ')', -1)

        return plaintext

    def __first_method(self, text, mode='enc'):
        delta = 1
        if mode == 'dec':
            delta = -1

        text = self.__remove_letters(text)

        enc_dec_text = []
        for letter in self.__remove_letters(text):
            result = np.array(letter)
            if np.isin(letter, self.eng_polybius_square):
                (i, j) = np.where(self.eng_polybius_square == letter)
                result = self.eng_polybius_square[(i + delta) % 5, j]
            elif np.isin(letter, self.rus_polybius_square):
                (i, j) = np.where(self.rus_polybius_square == letter)
                result = self.rus_polybius_square[(i + delta) % 5, j]
            enc_dec_text += result.tolist()

        return ''.join(enc_dec_text)

    def __remove_letters(self, text):
        if self.lang == 'ENG':
            return text.translate({ord(letter_fr): letter_to for letter_fr, letter_to in zip('J', 'I')})
        else:
            return text.translate({ord(letter_fr): letter_to for letter_fr, letter_to in zip('ЁЭЗЙСЩЪ', 'ЕЕЖИРШЬ')})

    def __insert_encoded_text(self, text_to_insert, encrypted_letters, indexes):
        encrypted_letters = ''.join(encrypted_letters)

        count = 0
        for start, end in indexes:
            text_to_insert = ''.join((text_to_insert[:start], encrypted_letters[count:count + end - start], text_to_insert[end:]))
            count += (end - start)

        return text_to_insert


# a = PolybiusSquare()
# print(a.encode('SOMETEXT', '2'))
# print(a.encode('SOMETEXT', '3'))
# print(a.decode('SWYSOCDU', '2'))
# print(a.decode('IUPTNQVO', '3'))