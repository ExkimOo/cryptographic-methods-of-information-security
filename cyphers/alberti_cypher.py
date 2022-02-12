import re

from widgets.constants import ENG_LETTERS, RUS_LETTERS


class Alberti:
    def encode(self, plaintext, key, lang='ENG'):
        if self.__is_correct_key(key, lang):
            alphabet = self.__generate_alphabet(key, lang)
            alphabet_length = len(alphabet)
            key_length = len(key)
            alphabet_number_letter_upper = {number: letter for number, letter in enumerate(alphabet)}
            alphabet_letter_number_upper = {letter: number for number, letter in enumerate(alphabet)}
            alphabet_number_letter_lower = {number: letter for number, letter in enumerate(alphabet.lower())}
            alphabet_letter_number_lower = {letter: number for number, letter in enumerate(alphabet.lower())}
            print(alphabet_number_letter_upper)
            print(plaintext)
            print(alphabet)

            cyphertext=''
            for i in range(len(plaintext)):
                result = plaintext[i]
                if plaintext[i] in alphabet_letter_number_upper.keys():
                    result = alphabet_number_letter_upper[
                        (alphabet_letter_number_upper[plaintext[i]] +
                         alphabet_letter_number_upper[key[i % key_length]]) % alphabet_length
                        ]
                    print(alphabet_letter_number_upper[plaintext[i]], key[i % key_length])
                elif plaintext[i] in alphabet_letter_number_lower.keys():
                    result = alphabet_number_letter_lower[
                        (alphabet_letter_number_lower[plaintext[i]] +
                         alphabet_letter_number_lower[key[i % key_length].lower()]) % alphabet_length
                        ]
                cyphertext += result

            return cyphertext

        return

    # def decode(self, cyphertext, key, lang='RUS'):
    #     if self.__is_correct_key(key, lang):
    #         key_length = len(key)
    #         plaintext = ''
    #         if lang == 'ENG':
    #             for i in range(len(cyphertext)):
    #                 result = cyphertext[i]
    #                 if cyphertext[i] in eng_letter_number_upper.keys():
    #                     result = eng_number_letter_upper[
    #                         (eng_letter_number_upper[cyphertext[i]] -
    #                          eng_letter_number_upper[key[i % key_length]]) % 26
    #                         ]
    #                 elif cyphertext[i] in eng_letter_number_lower.keys():
    #                     result = eng_number_letter_lower[
    #                         (eng_letter_number_lower[cyphertext[i]] -
    #                          eng_letter_number_lower[key[i % key_length].lower()]) % 26
    #                         ]
    #                 plaintext += result
    #         elif lang == 'RUS':
    #             for i in range(len(cyphertext)):
    #                 result = cyphertext[i]
    #                 if cyphertext[i] in rus_letter_number_upper.keys():
    #                     result = rus_number_letter_upper[
    #                         (rus_letter_number_upper[cyphertext[i]] -
    #                          rus_letter_number_upper[key[i % key_length]]) % 33
    #                         ]
    #                 elif cyphertext[i] in rus_letter_number_lower.keys():
    #                     result = rus_number_letter_lower[
    #                         (rus_letter_number_lower[cyphertext[i]] -
    #                          rus_letter_number_lower[key[i % key_length].lower()]) % 33
    #                         ]
    #                 plaintext += result
    #
    #         return plaintext
    #
    #     return

    def __generate_alphabet(self, key, lang):
        alphabet = ''
        if lang == 'ENG':
            LETTERS = ENG_LETTERS
        else:
            LETTERS = RUS_LETTERS

        for letter in key:
            if letter not in alphabet:
                alphabet += letter

        for letter in LETTERS:
            if letter not in alphabet:
                alphabet += letter

        return alphabet

    def __is_correct_key(self, key, lang):
        if re.match(r'^[A-Za-z]+$', key) and lang == 'ENG':
            return True
        if re.match(r'^[А-Яа-я]+$', key) and lang == 'RUS':
            return True
        return False

a = Alberti()
print(a.encode('HI', 'ACD', 'ENG'))