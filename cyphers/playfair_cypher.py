import numpy as np

from constants import RUS_LETTERS, ENG_LETTERS


class Playfair():
    def encode(self, plaintext, key, lang='ENG'):
        matrix = self.__generate_matrix(key, lang)
        cyphertext = ''
        print(plaintext)
        print(matrix)

        if lang == 'ENG':
            plaintext_without_repetitions = plaintext.replace('J', 'I')
            result = ''
            added_symbols = 0
            for i in range(0, len(plaintext_without_repetitions) - 1, 2):
                if plaintext_without_repetitions[i] == plaintext_without_repetitions[i + 1] and (i + added_symbols) % 2 == 0:
                    result += plaintext_without_repetitions[i] + 'X' + plaintext_without_repetitions[i + 1]
                    added_symbols += 1
                else:
                    result += plaintext_without_repetitions[i:i + 2]
            if len(plaintext_without_repetitions) % 2 == 1:
                result += plaintext[-1]
            plaintext_without_repetitions = result

            if len(plaintext_without_repetitions) % 2 == 1:
                plaintext_without_repetitions += 'X'

            for i in range(0, len(plaintext_without_repetitions), 2):
                (i1, j1) = map(int, np.where(plaintext_without_repetitions[i] == matrix))
                (i2, j2) = map(int, np.where(plaintext_without_repetitions[i + 1] == matrix))

                if i1 == i2:
                    cyphertext += (str(matrix[i1][(j1 + 1) % 5]) + str(matrix[i2][(j2 + 1) % 5]))
                elif j1 == j2:
                    cyphertext += (str(matrix[(i1 + 1) % 5][j1]) + str(matrix[(i2 + 1) % 5][j2]))
                else:
                    cyphertext += (str(matrix[i1][j2]) + str(matrix[i2][j1]))
        else:
            plaintext_without_repetitions = plaintext.replace('Ё', 'Е')
            result = ''
            added_symbols = 0
            for i in range(0, len(plaintext_without_repetitions) - 1, 2):
                if plaintext_without_repetitions[i] == plaintext_without_repetitions[i + 1] and (
                        i + added_symbols) % 2 == 0:
                    result += plaintext_without_repetitions[i] + 'Ъ' + plaintext_without_repetitions[i + 1]
                    added_symbols += 1
                else:
                    result += plaintext_without_repetitions[i:i + 2]
            if len(plaintext_without_repetitions) % 2 == 1:
                result += plaintext[-1]
            plaintext_without_repetitions = result

            if len(plaintext_without_repetitions) % 2 == 1:
                plaintext_without_repetitions += 'Ъ'

            for i in range(0, len(plaintext_without_repetitions), 2):
                (i1, j1) = map(int, np.where(plaintext_without_repetitions[i] == matrix))
                (i2, j2) = map(int, np.where(plaintext_without_repetitions[i + 1] == matrix))

                if i1 == i2:
                    cyphertext += (str(matrix[i1][(j1 + 1) % 8]) + str(matrix[i2][(j2 + 1) % 8]))
                elif j1 == j2:
                    cyphertext += (str(matrix[(i1 + 1) % 4][j1]) + str(matrix[(i2 + 1) % 4][j2]))
                else:
                    cyphertext += (str(matrix[i1][j2]) + str(matrix[i2][j1]))

        return cyphertext

    def decode(self, cyphertext, key, lang='ENG'):
        matrix = self.__generate_matrix(key, lang)
        plaintext = ''

        if lang == 'ENG':
            for i in range(0, len(cyphertext), 2):
                (i1, j1) = map(int, np.where(cyphertext[i] == matrix))
                (i2, j2) = map(int, np.where(cyphertext[i + 1] == matrix))

                if i1 == i2:
                    plaintext += (str(matrix[i1][(j1 - 1) % 5]) + str(matrix[i2][(j2 - 1) % 5]))
                elif j1 == j2:
                    plaintext += (str(matrix[(i1 - 1) % 5][j1]) + str(matrix[(i2 - 1) % 5][j2]))
                else:
                    plaintext += (str(matrix[i1][j2]) + str(matrix[i2][j1]))
        else:
            for i in range(0, len(cyphertext), 2):
                (i1, j1) = map(int, np.where(cyphertext[i] == matrix))
                (i2, j2) = map(int, np.where(cyphertext[i + 1] == matrix))

                if i1 == i2:
                    plaintext += (str(matrix[i1][(j1 - 1) % 8]) + str(matrix[i2][(j2 - 1) % 8]))
                elif j1 == j2:
                    plaintext += (str(matrix[(i1 - 1) % 4][j1]) + str(matrix[(i2 - 1) % 4][j2]))
                else:
                    plaintext += (str(matrix[i1][j2]) + str(matrix[i2][j1]))

        return plaintext


    def __generate_matrix(self, key, lang):
        matrix = ''
        if lang == 'ENG':
            for letter in key.replace('J', ''):
                if letter not in matrix:
                    matrix += letter

            for letter in ENG_LETTERS:
                if letter not in matrix:
                    matrix += letter

            matrix = np.array(list(matrix.replace('J', ''))).reshape((5, 5))
            print(matrix)
        else:
            for letter in key.replace('Ё', 'Е'):
                if letter not in matrix:
                    matrix += letter

            for letter in RUS_LETTERS:
                if letter not in matrix:
                    matrix += letter

            matrix = np.array(list(matrix.replace('Ё', ''))).reshape((4, 8))

        return matrix


# a = Playfair()
# print(a.encode('АТААКА', '', 'RUS'))
# print(a.decode('ВРВШВИВШ', '', 'RUS'))
# print(a.encode('IDIOCYOFTENLOOKSLIKEINTELLIGENCES', 'WHEATSON', 'ENG'))
# print(a.encode('IDIOCYOFTENLOOKSLIKEINTELLIGENCE', 'WHEATSON', 'ENG'))
# print(a.decode('KFFBBZFMWASPNVCFDUKDAGCEWPQDPNBSNE', 'WHEATSON', 'ENG'))
# print(a.decode('KFFBBZFMWASPNVCFDUKDAGCEWPQDPNBSWN', 'WHEATSON', 'ENG'))