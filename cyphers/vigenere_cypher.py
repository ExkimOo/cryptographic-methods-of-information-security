import re

from constants.constants import ENG_LETTERS, RUS_LETTERS


class Vigenere:
    def __init__(self):
        self.ENG_LETTERS = ENG_LETTERS
        self.ENG_LETTERS_LOWER = ENG_LETTERS.lower()
        self.RUS_LETTERS = RUS_LETTERS
        self.RUS_LETTERS_LOWER = RUS_LETTERS.lower()

    def encode(self, plaintext, key):
        return self.__enc_dec(plaintext, key)

    def decode(self, cyphertext, key):
        return self.__enc_dec(cyphertext, key, 'dec')

    def __enc_dec(self, text, key, method='enc'):
        key_lang = self.__is_correct_key(key.upper())
        if not key_lang:
            print('Неверный ключ')
            return

        key_vector = self.__key_to_numbers_vector(key, key_lang)
        key_length = len(key_vector)

        enc_dec_text = ''
        for i in range(len(text)):
            result = text[i]

            k_index = key_vector[i % key_length]
            if method == 'dec':
                k_index = -k_index

            if text[i] in self.ENG_LETTERS:
                t_index = self.ENG_LETTERS.index(text[i])
                result = self.ENG_LETTERS[(t_index + k_index) % 26]
            elif text[i] in self.ENG_LETTERS_LOWER:
                t_index = self.ENG_LETTERS_LOWER.index(text[i])
                result = self.ENG_LETTERS_LOWER[(t_index + k_index) % 26]
            elif text[i] in self.RUS_LETTERS:
                t_index = self.RUS_LETTERS.index(text[i])
                result = self.RUS_LETTERS[(t_index + k_index) % 33]
            elif text[i] in self.RUS_LETTERS_LOWER:
                t_index = self.RUS_LETTERS_LOWER.index(text[i])
                result = self.RUS_LETTERS_LOWER[(t_index + k_index) % 33]

            enc_dec_text += result

        return enc_dec_text

    def __key_to_numbers_vector(self, key, key_lang):
        key_vector = []
        if key_lang == 'ENG':
            for letter in key.upper():
                key_vector.append(self.ENG_LETTERS.index(letter))
        else:
            for letter in key.upper():
                key_vector.append(self.RUS_LETTERS.index(letter))

        return key_vector

    def __is_correct_key(self, key):
        if re.match(r'^[A-Za-z]+$', key):
            return 'ENG'
        if re.match(r'^[А-Яа-яЕё]+$', key):
            return 'RUS'
        return False

# a = Vigenere('RUS')
# print(a.encode('АТАКАНАРАССВЕТЕатаканарассвете', 'ЛЕМОННасу'))
# print(a.decode('ЛЧМЩНЫАВУЭЦОУАТадуцеъоюнсгхрчс', 'ЛЕМОННасу'))
#
# a = Vigenere('ENG')
# print(a.encode('ATTACKATDAWN   attackatdawn', 'LEMON'))
# print(a.decode('LXFOPVEFRNHR   lxfopvefrnhr', 'LEMON'))