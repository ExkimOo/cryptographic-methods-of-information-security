from widgets.constants import \
    eng_number_letter_upper, eng_letter_number_upper, \
    rus_letter_number_upper, rus_number_letter_upper, \
    eng_letter_number_lower, eng_number_letter_lower, \
    rus_letter_number_lower, rus_number_letter_lower


class Gronsfeld():
    def encode(self, plaintext, key):
        key = (key * (len(plaintext) // len(key) + 1))[:len(plaintext)]
        cyphertext = ''
        for letter, number in zip(plaintext, key):
            result = letter
            if letter in eng_letter_number_upper.keys():
                result = eng_number_letter_upper[eng_letter_number_upper[letter] + int(number)]
            elif letter in eng_letter_number_lower.keys():
                result = eng_number_letter_lower[eng_letter_number_lower[letter] + int(number)]
            elif letter in rus_letter_number_upper.keys():
                result = rus_number_letter_upper[rus_letter_number_upper[letter] + int(number)]
            elif letter in rus_letter_number_lower.keys():
                result = rus_number_letter_lower[rus_letter_number_lower[letter] + int(number)]
            cyphertext += result

        return cyphertext

    def decode(self, cyphertext, key):
        key = (key * (len(cyphertext) // len(key) + 1))[:len(cyphertext)]
        plaintext = ''
        for letter, number in zip(cyphertext, key):
            result = letter
            if letter in eng_letter_number_upper.keys():
                result = eng_number_letter_upper[eng_letter_number_upper[letter] - int(number)]
            elif letter in eng_letter_number_lower.keys():
                result = eng_number_letter_lower[eng_letter_number_lower[letter] - int(number)]
            elif letter in rus_letter_number_upper.keys():
                result = rus_number_letter_upper[rus_letter_number_upper[letter] - int(number)]
            elif letter in rus_letter_number_lower.keys():
                result = rus_number_letter_lower[rus_letter_number_lower[letter] - int(number)]
            plaintext += result

        return plaintext


# a = Gronsfeld()
# print(a.encode('hellHELLпривПРИВ', '2015'))
# print(a.decode('jemqJEMQсрйжСРЙЖ', '2015'))