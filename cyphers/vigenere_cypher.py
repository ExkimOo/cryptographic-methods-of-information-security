import re

from widgets.constants import ENG_LETTERS, RUS_LETTERS


class Vigenere:
    def __init__(self, lang='ENG'):
        self.lang = lang

        if lang == 'ENG':
            self.LETTERS = ENG_LETTERS
            self.LETTERS_LOWER = ENG_LETTERS.lower()
        else:
            self.LETTERS = RUS_LETTERS
            self.LETTERS_LOWER = RUS_LETTERS.lower()

        self.modulo = len(self.LETTERS)

    def encode(self, plaintext, key):
        if not self.__is_correct_key(key):
            return

        return self.__enc_dec(plaintext, key)

    def decode(self, cyphertext, key):
        if not self.__is_correct_key(key):
            return

        return self.__enc_dec(cyphertext, key, 'dec')

    def __enc_dec(self, text, key, method='enc'):
        key_length = len(key)
        enc_dec_text = ''

        for i in range(len(text)):
            result = text[i]
            if text[i] in self.LETTERS:
                t_index = self.LETTERS.index(text[i])
                k_index = self.LETTERS.index(key[i % key_length].upper())

                if method == 'dec':
                    k_index = -k_index

                result = self.LETTERS[(t_index + k_index) % self.modulo]
            elif text[i] in self.LETTERS_LOWER:
                t_index = self.LETTERS_LOWER.index(text[i])
                k_index = self.LETTERS_LOWER.index(key[i % key_length].lower())

                if method == 'dec':
                    k_index = -k_index

                result = self.LETTERS_LOWER[(t_index + k_index) % self.modulo]

            enc_dec_text += result

        return enc_dec_text

    def __is_correct_key(self, key):
        if re.match(r'^[A-Za-z]+$', key) and self.lang == 'ENG':
            return True
        if re.match(r'^[А-Яа-я]+$', key) and self.lang == 'RUS':
            return True
        return False

# a = Vigenere('RUS')
# print(a.encode('АТАКАНАРАССВЕТЕатаканарассвете', 'ЛЕМОННасу'))
# print(a.decode('ЛЧМЩНЫАВУЭЦОУАТадуцеъоюнсгхрчс', 'ЛЕМОННасу'))
#
# a = Vigenere('ENG')
# print(a.encode('ATTACKATDAWN   attackatdawn', 'LEMON'))
# print(a.decode('LXFOPVEFRNHR   lxfopvefrnhr', 'LEMON'))