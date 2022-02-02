# import re
from constants import eng_number_letter_upper, eng_letter_number_upper


class Vigenere:
    # def __init__(self, key, plaintext=None, cyphertext=None):
    #     if re.match(r'[A-Z]+', plaintext) and re.match(r'[A-Z]+', key):
    #         self.plaintext = plaintext
    #         self.key = key
    #         self.cyphertext = ''

    def encode(self, plaintext, key):
        key_length = len(key)
        cyphertext=''
        for i in range(len(plaintext)):
            result = eng_number_letter_upper[(eng_letter_number_upper[plaintext[i]] + eng_letter_number_upper[key[i % key_length]]) % 26]
            cyphertext += result

        return cyphertext

    def decode(self, cyphertext, key):
        key_length = len(key)
        plaintext = ''
        for i in range(len(cyphertext)):
            result = eng_number_letter_upper[(eng_letter_number_upper[cyphertext[i]] - eng_letter_number_upper[key[i % key_length]]) % 26]
            plaintext += result

        return plaintext

# a = Vigenere()
# print(a.encode('ATTACKATDAWN', 'LEMON'))
# print(a.decode('LXFOPVEFRNHR', 'LEMON'))