from functools import reduce


class Vernam():
    def encode(self, plaintext, key):
        if self.__is_correct_key(plaintext, key):
            plaintext_bin = reduce(lambda x,y: x + y, [bin(ord(letter))[2:].zfill(8) for letter in plaintext])
            cyphertext = ''
            for i in range(0, len(key), 8):
                cyphertext += chr(int(plaintext_bin[i:i+8], 2) ^ int(key[i:i+8], 2))

            return cyphertext

    def decode(self, cyphertext, key):
        if self.__is_correct_key(cyphertext, key):
            cyphertext_bin = reduce(lambda x,y: x + y, [bin(ord(letter))[2:].zfill(8) for letter in cyphertext])
            plaintext = ''
            for i in range(0, len(key), 8):
                plaintext += chr(int(cyphertext_bin[i:i+8], 2) ^ int(key[i:i+8], 2))

            return plaintext

    def __is_correct_key(self, plaintext, key):
        if len(key) < len(plaintext)*8:
            print('Длина ключа в должна быть не меньше длины сообщения в бинарном виде')
            return False
        return True


# a = Vernam()
# print(a.encode('KOD', '101011010111101010101011'))
# print(a.decode('æ5ï', '101011010111101010101011'))


