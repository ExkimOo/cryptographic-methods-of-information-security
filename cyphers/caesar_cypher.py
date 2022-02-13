import re

from widgets.constants import RUS_LETTERS, ENG_LETTERS


class Ceasar:
    def encode(self, plaintext, key):
        if not self.__is_correct_key(key):
            return

        key = int(key)
        return self.__enc_dec(plaintext, key)

    def decode(self, cyphertext, key):
        if not self.__is_correct_key(key):
            return

        key = -int(key)
        return self.__enc_dec(cyphertext, key)

    def __enc_dec(self, text, key):
        enc_dec_text = ''
        for letter in text:
            result = letter
            if letter in ENG_LETTERS:
                result = ENG_LETTERS[(ENG_LETTERS.index(letter) + key) % 26]
            elif letter in ENG_LETTERS.lower():
                result = ENG_LETTERS.lower()[(ENG_LETTERS.lower().index(letter) + key) % 26]
            elif letter in RUS_LETTERS:
                result = RUS_LETTERS[(RUS_LETTERS.index(letter) + key) % 33]
            elif letter in RUS_LETTERS.lower():
                result = RUS_LETTERS.lower()[(RUS_LETTERS.lower().index(letter) + key) % 33]
            enc_dec_text += result

        return enc_dec_text

    def __is_correct_key(self, m):
        if re.match(r'^[0-9]{1,33}$', m):
            return True
        return False

# a = Ceasar()
# print(a.encode('ABC abc ЭЮЯ эюя', '11'))
# print(a.decode('LMN lmn ЗИЙ зий', '11'))