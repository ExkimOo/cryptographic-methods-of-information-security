from widgets.constants import \
    eng_number_letter_upper, eng_letter_number_upper, \
    rus_letter_number_upper, rus_number_letter_upper, \
    eng_letter_number_lower, eng_number_letter_lower, \
    rus_letter_number_lower, rus_number_letter_lower


class Vigenere:
    def encode(self, plaintext, key, lang='EN'):
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
        else:
            for i in range(len(plaintext)):
                if plaintext[i] in rus_letter_number_upper.keys():
                    result = rus_number_letter_upper[
                        (rus_letter_number_upper[plaintext[i]] +
                         rus_letter_number_upper[key[i % key_length]]) % 26
                        ]
                elif plaintext[i] in rus_letter_number_lower.keys():
                    result = rus_number_letter_lower[
                        (rus_letter_number_lower[plaintext[i]] +
                         rus_letter_number_lower[key[i % key_length].lower()]) % 26
                        ]
                cyphertext += result

        return cyphertext

    def decode(self, cyphertext, key, lang='RUS'):
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
        else:
            for i in range(len(cyphertext)):
                result = cyphertext[i]
                if cyphertext[i] in rus_letter_number_upper.keys():
                    result = rus_number_letter_upper[
                        (rus_letter_number_upper[cyphertext[i]] -
                         rus_letter_number_upper[key[i % key_length]]) % 26
                        ]
                elif cyphertext[i] in rus_letter_number_lower.keys():
                    result = rus_number_letter_lower[
                        (rus_letter_number_lower[cyphertext[i]] -
                         rus_letter_number_lower[key[i % key_length].lower()]) % 26
                        ]
                plaintext += result

        return plaintext

# a = Vigenere()
# print(a.encode('ATTACKATDAWN   attackatdawn', 'LEMON', 'ENG'))
# print(a.decode('LXFOPVEFRNHR   lxfopvefrnhr', 'LEMON', 'ENG'))
# print(a.encode('АТАКАНАРАССВЕТЕатаканарассвете', 'ЛЕМОН', 'RUS'))
# print(a.decode('ЛЧМАНАЕДОЁДЖСЗТлчманаедоёджсзт', 'ЛЕМОН', 'RUS'))