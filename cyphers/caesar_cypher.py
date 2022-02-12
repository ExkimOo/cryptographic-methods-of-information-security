import re

from widgets.constants import \
    eng_number_letter_upper, eng_letter_number_upper, \
    rus_letter_number_upper, rus_number_letter_upper, \
    eng_letter_number_lower, eng_number_letter_lower, \
    rus_letter_number_lower, rus_number_letter_lower


class Ceasar:
    def encode(self, plaintext, key):
        cyphertext = ''
        key = self.__is_correct_key(key)
        if key:
            for letter in plaintext:
                result = letter
                if letter in eng_letter_number_upper.keys():
                    result = eng_number_letter_upper[(eng_letter_number_upper[letter] + key) % 26]
                elif letter in eng_letter_number_lower.keys():
                    result = eng_number_letter_lower[(eng_letter_number_lower[letter] + key) % 26]
                elif letter in rus_letter_number_upper.keys():
                    result = rus_number_letter_upper[(rus_letter_number_upper[letter] + key) % 33]
                elif letter in rus_letter_number_lower.keys():
                    result = rus_number_letter_lower[(rus_letter_number_lower[letter] + key) % 33]
                cyphertext += result

            return cyphertext
        return

    def decode(self, cyphertext, key):
        plaintext = ''
        key = self.__is_correct_key(key)
        if key:
            for letter in cyphertext:
                result = letter
                if letter in eng_letter_number_upper.keys():
                    result = eng_number_letter_upper[(eng_letter_number_upper[letter] - key) % 26]
                elif letter in eng_letter_number_lower.keys():
                    result = eng_number_letter_lower[(eng_letter_number_lower[letter] - key) % 26]
                elif letter in rus_letter_number_upper.keys():
                    result = rus_number_letter_upper[(rus_letter_number_upper[letter] - key) % 33]
                elif letter in rus_letter_number_lower.keys():
                    result = rus_number_letter_lower[(rus_letter_number_lower[letter] - key) % 33]
                plaintext += result

            return plaintext
        return

    def __is_correct_key(self, m):
        if re.match(r'^[0-9]+$', m):
            return int(m)
        return False

# a = Ceasar()
# print(a.encode('ABC abc ЭЮЯ эюя', 1))
# print(a.decode('BCD bcd ЮЯА юяа', 1))