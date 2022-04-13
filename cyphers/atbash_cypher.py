from constants.constants import ENG_LETTERS, RUS_LETTERS


class Atbash:
    def encode(self, plaintext):
        return self.__encrypt_decrypt(plaintext)

    def decode(self, cyphertext):
        return self.__encrypt_decrypt(cyphertext)

    def __encrypt_decrypt(self, text):
        enc_dec_text = ''
        for letter in text:
            result = letter
            if letter in ENG_LETTERS:
                result = ENG_LETTERS[25 - ENG_LETTERS.index(letter)]
            elif letter in ENG_LETTERS.lower():
                result = ENG_LETTERS.lower()[25 - ENG_LETTERS.lower().index(letter)]
            elif letter in RUS_LETTERS:
                result = RUS_LETTERS[32 - RUS_LETTERS.index(letter)]
            elif letter in RUS_LETTERS.lower():
                result = RUS_LETTERS.lower()[32 - RUS_LETTERS.lower().index(letter)]
            enc_dec_text += result

        return enc_dec_text

# a = Atbash()
# print(a.encode('hello HELLO привет ПРИВЕТ'))
# print(a.decode('svool SVOOL поцэъм ПОЦЭЪМ'))
