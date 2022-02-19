import re
from functools import reduce


class Vernam():
    def encode(self, plaintext, key):
        if not self.__is_correct_key(plaintext, key):
            return

        return self.__enc_dec(plaintext, key)

    def decode(self, cyphertext, key):
        if not self.__is_correct_key(cyphertext, key):
            return

        return self.__enc_dec(cyphertext, key)

    def __enc_dec(self, text, key):
        text_bin = reduce(lambda x, y: x + y, [bin(ord(letter))[2:].zfill(8) for letter in text])
        enc_dec_text = ''
        for i in range(0, len(text)*8, 8):
            enc_dec_text += chr(int(text_bin[i:i + 8], 2) ^ int(key[i:i + 8], 2))

        return enc_dec_text

    def __is_correct_key(self, text, key):
        if not re.match(r'^[01]+$', key):
            print('Ключ содержит недопустимые символы')
            return False

        if len(key) < len(text)*8:
            print('Длина ключа в должна быть не меньше длины сообщения в бинарном виде')
            return False

        return True