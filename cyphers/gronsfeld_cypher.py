import re

from widgets.constants import ENG_LETTERS, RUS_LETTERS


class Gronsfeld():
    def encode(self, plaintext, key):
        return self.__enc_dec(plaintext, key)

    def decode(self, cyphertext, key):
        return self.__enc_dec(cyphertext, key, 'dec')

    def __enc_dec(self, text, key, method='enc'):
        if not self.__is_correct_key(key):
            return

        key = (key * (len(text) // len(key) + 1))[:len(text)]
        enc_dec_text = ''
        for letter, number in zip(text, key):

            if method == 'dec':
                number = '-' + number

            result = letter
            if letter in ENG_LETTERS:
                result = ENG_LETTERS[(ENG_LETTERS.index(letter) + int(number)) % 26]
            elif letter in ENG_LETTERS.lower():
                result = ENG_LETTERS.lower()[(ENG_LETTERS.lower().index(letter) + int(number)) % 26]
            elif letter in RUS_LETTERS:
                result = RUS_LETTERS[(RUS_LETTERS.index(letter) + int(number)) % 33]
            elif letter in RUS_LETTERS.lower():
                result = RUS_LETTERS.lower()[(RUS_LETTERS.lower().index(letter) + int(number)) % 33]
            enc_dec_text += result

        return enc_dec_text

    def __is_correct_key(self, key):
        if re.match(r'^[0-9]{1,100}$', key):
            return True
        return False

# a = Gronsfeld()XYz 123 ЭЮя
# print(a.encode('hellHELLпривПРИВ', '2015'))
# print(a.decode('jemqJEMQсрйжСРЙЖ', '2015'))