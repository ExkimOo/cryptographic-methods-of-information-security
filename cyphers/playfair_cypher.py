import re

import numpy as np

from widgets.constants import RUS_LETTERS, ENG_LETTERS


class Playfair():
    def __init__(self, lang, key):
        self.lang = lang
        self.key = key.upper().replace('J', 'I').replace('Ё', 'Е')

    def encode(self, plaintext):
        plaintext = self.__remove_letters(plaintext)
        return self.__enc_dec(plaintext, 'enc')

    def decode(self, cyphertext):
        return self.__enc_dec(cyphertext, 'dec')

    def __enc_dec(self, text, method):
        if not self.__is_correct_key():
            return

        if not self.__is_correct_text(text):
            return

        matrix = self.generate_matrix()
        text = text.upper().replace('J', 'I').replace('Ё', 'Е')

        if self.lang == 'ENG':
            row_len = 5
            col_len = 5
            rare_letter = 'X'
        else:
            row_len = 4
            col_len = 8
            rare_letter = 'Ъ'

        incr_decr = 1
        if method == 'dec':
            incr_decr = -1

        while True:
            indexes = [(m.start(0), m.end(0)) for m in re.finditer(r'([A-Za-z])\1', text) if m.start(0) % 2 == 0]
            if not indexes:
                break
            text = ''.join((text[:indexes[0][0] + 1], rare_letter, text[indexes[0][1] - 1:]))

        if len(text) % 2 == 1:
            text += rare_letter

        enc_dec_text = ''
        for i in range(0, len(text), 2):
            (i1, j1) = map(int, np.where(text[i] == matrix))
            (i2, j2) = map(int, np.where(text[i + 1] == matrix))

            if i1 == i2:
                enc_dec_text += (str(matrix[i1][(j1 + incr_decr) % col_len]) +
                                 str(matrix[i2][(j2 + incr_decr) % col_len]))
            elif j1 == j2:
                enc_dec_text += (str(matrix[(i1 + incr_decr) % row_len][j1]) +
                                 str(matrix[(i2 + incr_decr) % row_len][j2]))
            else:
                enc_dec_text += (str(matrix[i1][j2]) + str(matrix[i2][j1]))

        return enc_dec_text

    def generate_matrix(self):
        matrix = ''
        if self.lang == 'ENG':
            for letter in self.key.replace('J', ''):
                if letter not in matrix:
                    matrix += letter

            for letter in ENG_LETTERS:
                if letter not in matrix:
                    matrix += letter

            matrix = np.array(list(matrix.replace('J', ''))).reshape((5, 5))
        else:
            for letter in self.key.replace('Ё', 'Е'):
                if letter not in matrix:
                    matrix += letter

            for letter in RUS_LETTERS:
                if letter not in matrix:
                    matrix += letter

            matrix = np.array(list(matrix.replace('Ё', ''))).reshape((4, 8))

        return matrix

    def __remove_letters(self, text):
        if self.lang == 'ENG':
            text = ''.join([letter for letter in text.upper() if letter in ENG_LETTERS])
        else:
            text = ''.join([letter for letter in text.upper() if letter in RUS_LETTERS])

        return text

    def __is_correct_key(self):
        if self.lang == 'ENG' and re.match(r'^[A-Za-z]*$', self.key):
            return True
        elif self.lang == 'RUS' and re.match(r'^[А-Яа-яЁё]*$', self.key):
            return True
        else:
            print('Неправильный ключ')
            return

    def __is_correct_text(self, text):
        if self.lang == 'ENG' and re.match(r'^[A-Za-z]+$', text):
            return True
        elif self.lang == 'RUS' and re.match(r'^[А-Яа-яЁё]+$', text):
            return True
        else:
            print('Неправильный текст')
            return