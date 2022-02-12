import re

from widgets.constants import \
    eng_number_letter_upper, eng_letter_number_upper, \
    rus_letter_number_upper, rus_number_letter_upper, \
    eng_letter_number_lower, eng_number_letter_lower, \
    rus_letter_number_lower, rus_number_letter_lower


class Vigenere:
    def encode(self, plaintext, key, lang='ENG'):
        if self.__is_correct_key(key, lang):
            key_length = len(key)
            cyphertext=''
            if lang == 'ENG':
                for i in range(len(plaintext)):
                    result = plaintext[i]
                    if plaintext[i] in eng_letter_number_upper.keys():
                        result = eng_number_letter_upper[
                            (eng_letter_number_upper[plaintext[i]] +
                             eng_letter_number_upper[key[i % key_length]]) % 26
                            ]
                    elif plaintext[i] in eng_letter_number_lower.keys():
                        result = eng_number_letter_lower[
                            (eng_letter_number_lower[plaintext[i]] +
                             eng_letter_number_lower[key[i % key_length].lower()]) % 26
                            ]
                    cyphertext += result
            elif lang == 'RUS':
                for i in range(len(plaintext)):
                    result = plaintext[i]
                    if plaintext[i] in rus_letter_number_upper.keys():
                        result = rus_number_letter_upper[
                            (rus_letter_number_upper[plaintext[i]] +
                             rus_letter_number_upper[key[i % key_length]]) % 33
                            ]
                    elif plaintext[i] in rus_letter_number_lower.keys():
                        result = rus_number_letter_lower[
                            (rus_letter_number_lower[plaintext[i]] +
                             rus_letter_number_lower[key[i % key_length].lower()]) % 33
                            ]
                    cyphertext += result

            return cyphertext

        return

    def decode(self, cyphertext, key, lang='RUS'):
        if self.__is_correct_key(key, lang):
            key_length = len(key)
            plaintext = ''
            if lang == 'ENG':
                for i in range(len(cyphertext)):
                    result = cyphertext[i]
                    if cyphertext[i] in eng_letter_number_upper.keys():
                        result = eng_number_letter_upper[
                            (eng_letter_number_upper[cyphertext[i]] -
                             eng_letter_number_upper[key[i % key_length]]) % 26
                            ]
                    elif cyphertext[i] in eng_letter_number_lower.keys():
                        result = eng_number_letter_lower[
                            (eng_letter_number_lower[cyphertext[i]] -
                             eng_letter_number_lower[key[i % key_length].lower()]) % 26
                            ]
                    plaintext += result
            elif lang == 'RUS':
                for i in range(len(cyphertext)):
                    result = cyphertext[i]
                    if cyphertext[i] in rus_letter_number_upper.keys():
                        result = rus_number_letter_upper[
                            (rus_letter_number_upper[cyphertext[i]] -
                             rus_letter_number_upper[key[i % key_length]]) % 33
                            ]
                    elif cyphertext[i] in rus_letter_number_lower.keys():
                        result = rus_number_letter_lower[
                            (rus_letter_number_lower[cyphertext[i]] -
                             rus_letter_number_lower[key[i % key_length].lower()]) % 33
                            ]
                    plaintext += result

            return plaintext

        return

    def __is_correct_key(self, key, lang):
        if re.match(r'^[A-Za-z]+$', key) and lang == 'ENG':
            return True
        if re.match(r'^[А-Яа-я]+$', key) and lang == 'RUS':
            return True
        return False

# a = Vigenere()
# print(a.encode('ATTACKATDAWN   attackatdawn', 'LEMON', 'ENG'))
# print(a.decode('LXFOPVEFRNHR   lxfopvefrnhr', 'LEMON', 'ENG'))
# print(a.encode('АТАКАНАРАССВЕТЕатаканарассвете', 'ЛЕМОН', 'RUS'))
# print(a.decode('ЛЧМАНАЕДОЁДЖСЗТлчманаедоёджсзт', 'ЛЕМОН', 'RUS'))
# print(a.encode('афым', 'афыа', 'RUS'))