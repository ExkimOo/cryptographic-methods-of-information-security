from constants import \
    eng_number_letter_upper, eng_letter_number_upper, \
    rus_letter_number_upper, rus_number_letter_upper, \
    eng_letter_number_lower, eng_number_letter_lower, \
    rus_letter_number_lower, rus_number_letter_lower


class Atbash:
    def encode(self, plaintext):
        cyphertext = ''
        for letter in plaintext:
            result = letter
            if letter in eng_letter_number_upper.keys():
                result = eng_number_letter_upper[25 - eng_letter_number_upper[letter]]
            elif letter in eng_letter_number_lower.keys():
                result = eng_number_letter_lower[25 - eng_letter_number_lower[letter]]
            elif letter in rus_letter_number_upper.keys():
                result = rus_number_letter_upper[32 - rus_letter_number_upper[letter]]
            elif letter in rus_letter_number_lower.keys():
                result = rus_number_letter_lower[32 - rus_letter_number_lower[letter]]
            cyphertext += result

        return cyphertext

    def decode(self, cyphertext):
        plaintext = ''
        for letter in cyphertext:
            result = letter
            if letter in eng_letter_number_upper.keys():
                result = eng_number_letter_upper[25 - eng_letter_number_upper[letter]]
            elif letter in eng_letter_number_lower.keys():
                result = eng_number_letter_lower[25 - eng_letter_number_lower[letter]]
            elif letter in rus_letter_number_upper.keys():
                result = rus_number_letter_upper[32 - rus_letter_number_upper[letter]]
            elif letter in rus_letter_number_lower.keys():
                result = rus_number_letter_lower[32 - rus_letter_number_lower[letter]]
            plaintext += result

        return plaintext

# a = Atbash()
# print(a.encode('hello HELLO привет ПРИВЕТ'))
# print(a.decode('svool SVOOL поцэъм ПОЦЭЪМ'))
