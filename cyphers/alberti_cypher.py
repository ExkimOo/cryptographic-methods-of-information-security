from constants.constants import ENG_LETTERS, RUS_LETTERS

import re


class Alberti:
    def __init__(self, key, shift, lang='ENG'):
        self.lang = lang
        self.shift = int(shift)
        self.inside_alphabet, self.outside_alphabet = self.__generate_alphabet(key)
        self.inside_alphabet_lower = self.inside_alphabet.lower()
        self.outside_alphabet_lower = self.outside_alphabet.lower()

    def encrypt(self, plaintext):
        inside_alphabet = self.inside_alphabet

        cyphertext = ''
        for letter in plaintext:
            result = letter
            if letter in self.outside_alphabet:
                result = inside_alphabet[(self.outside_alphabet.index(letter)) % len(inside_alphabet)]
            elif letter in self.outside_alphabet_lower:
                result = inside_alphabet.lower()[(self.outside_alphabet_lower.index(letter)) % len(inside_alphabet)]

            inside_alphabet = inside_alphabet[self.shift:] + inside_alphabet[:self.shift]

            cyphertext += result

        return cyphertext

    def decrypt(self, cyphertext):
        inside_alphabet = self.inside_alphabet

        plaintext = ''
        for letter in cyphertext:
            result = letter
            if letter in self.outside_alphabet:
                result = self.outside_alphabet[inside_alphabet.index(letter) % len(inside_alphabet)]
            elif letter in self.outside_alphabet_lower:
                result = self.outside_alphabet_lower[(inside_alphabet.lower().index(letter)) % len(inside_alphabet)]

            inside_alphabet = inside_alphabet[self.shift:] + inside_alphabet[:self.shift]

            plaintext += result

        return plaintext

    def __generate_alphabet(self, key):
        if self.lang == 'ENG':
            if self.__is_correct_key(key):
                alphabet = ''
                for letter in key.upper():
                    if letter not in alphabet:
                        alphabet += letter

                for letter in ENG_LETTERS:
                    if letter not in alphabet:
                        alphabet += letter

                return alphabet, ENG_LETTERS
            else:
                return ENG_LETTERS, ENG_LETTERS
        else:
            if self.__is_correct_key(key):
                alphabet = ''
                for letter in key.upper():
                    if letter not in alphabet:
                        alphabet += letter

                for letter in RUS_LETTERS:
                    if letter not in alphabet:
                        alphabet += letter

                return alphabet, RUS_LETTERS
            else:
                return RUS_LETTERS, RUS_LETTERS

    def __is_correct_key(self, key):
        if re.match(r'^[A-Za-z]*$', key) and self.lang == 'ENG':
            return True
        if re.match(r'^[А-Яа-яЕё]+$', key) and self.lang == 'RUS':
            return True
        return False