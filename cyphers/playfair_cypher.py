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
        enc_dec_text = ''
        text = text.upper()

        if self.lang == 'ENG':
            text_without_repetitions = text.replace('J', 'I')
            rare_letter = 'X'
            row_len = 5
            col_len = 5
        else:
            text_without_repetitions = text.replace('Ё', 'Е')
            rare_letter = 'Ъ'
            row_len = 4
            col_len = 8

        incr_decr = 1
        if method == 'dec':
            incr_decr = -1

        result = ''
        added_symbols = 0
        for i in range(0, len(text_without_repetitions) - 1, 2):
            if text_without_repetitions[i] == text_without_repetitions[i + 1] and (i + added_symbols) % 2 == 0:
                result += text_without_repetitions[i] + rare_letter + text_without_repetitions[i + 1]
                added_symbols += 1
            else:
                result += text_without_repetitions[i:i + 2]

        if len(text_without_repetitions) % 2 == 1:
            result += text[-1]
        text_without_repetitions = result

        if len(text_without_repetitions) % 2 == 1:
            text_without_repetitions += rare_letter

        for i in range(0, len(text_without_repetitions), 2):
            (i1, j1) = map(int, np.where(text_without_repetitions[i] == matrix))
            (i2, j2) = map(int, np.where(text_without_repetitions[i + 1] == matrix))

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
        if self.lang == 'ENG' and re.match(r'^[A-Z]*$', self.key):
            return True
        elif self.lang == 'RUS' and re.match(r'^[А-Я]*$', self.key):
            return True
        else:
            print('Неправильный ключ')
            return

    def __is_correct_text(self, text):
        if self.lang == 'ENG' and re.match(r'^[A-Za-z]+$', text):
            return True
        elif self.lang == 'RUS' and re.match(r'^[А-Яа-я]+$', text):
            return True
        else:
            print('Неправильный текст')
            return

# a = Playfair('ENG', 'WHEATSON')
# print(a.encode('IDIOCYOFTENLOOKSLIKEINTELLIGENCES'))
# print(a.encode('IDIOCYOFTENLOOKSLIKEINTELLIGENCE'))
# print(a.decode('KFFBBZFMWASPNVCFDUKDAGCEWPQDPNBSNE'))
# print(a.decode('KFFBBZFMWASPNVCFDUKDAGCEWPQDPNBSWN'))
#
# a = Playfair('RUS')
# print(a.encode('АТААКА', ''))
# print(a.decode('ВРВШВИВШ', ''))
