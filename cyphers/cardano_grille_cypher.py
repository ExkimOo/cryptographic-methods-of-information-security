from random import randint
from random import choice

import numpy as np


class CardanoGrille():
    def __init__(self, size, jumbled=True):
        self.size = size
        self.grille = self.__generate_grille()
        self.jumbled = jumbled

    def encode(self, plaintext):
        num_of_posiitons = int(np.max(self.grille))
        max_len = num_of_posiitons*4
        blocks = [plaintext[i:i + max_len] for i in range(0, len(plaintext), max_len)]

        cyphertext_matrix = np.empty((self.size, self.size), dtype=str)
        cyphertext_matrix.fill('')

        cyphertext = []
        for block in blocks:
            for rotation in range(4):
                grill_rotated = np.rot90(self.grille, k=-rotation)
                for position in range(1, num_of_posiitons + 1):
                    if rotation*num_of_posiitons + position > len(block):
                        break
                    (i, j) = np.where(position == grill_rotated)
                    cyphertext_matrix[i, j] = block[rotation*num_of_posiitons + position - 1]

            indexes = np.where(cyphertext_matrix == '')
            if self.jumbled:
                letters = [choice(block) for _ in range(len(indexes[0]))]
                cyphertext_matrix[indexes] = letters
            else:
                cyphertext_matrix[indexes] = ' '

            cyphertext += cyphertext_matrix.flatten().tolist()

        return ''.join(cyphertext)

    def decode(self, cyphertext):
        if cyphertext == '':
            return

        num_of_posiitons = int(np.max(self.grille))
        max_len = self.size**2
        blocks = [cyphertext[i:i + max_len] for i in range(0, len(cyphertext), max_len)]
        blocks[-1] += ' '*(max_len - len(blocks[-1]))

        plaintext = []
        for block in blocks:
            block_matrix = np.array(list(block)).reshape((self.size, self.size))
            for rotation in range(4):
                grill_rotated = np.rot90(self.grille, k=-rotation)
                for position in range(1, num_of_posiitons + 1):
                    if rotation * num_of_posiitons + position > len(block):
                        break
                    (i, j) = np.where(position == grill_rotated)
                    plaintext += block_matrix[i[0], j[0]]

        return ''.join(plaintext)

    def whole_grille(self):
        grille = np.copy(self.grille)
        for rotation in range(4):
            indexes = np.where(np.rot90(grille, k=-rotation) != 0)
            grille[indexes] = np.rot90(grille, k=-rotation)[indexes]

        return grille

    def __generate_grille(self):
        grille = np.zeros((self.size, self.size))
        rotated_grills = [
            np.arange(self.size ** 2).reshape((self.size, self.size)),
            np.rot90(np.arange(self.size ** 2).reshape((self.size, self.size)), k=-1),
            np.rot90(np.arange(self.size ** 2).reshape((self.size, self.size)), k=-2),
            np.rot90(np.arange(self.size ** 2).reshape((self.size, self.size)), k=-3)
        ]

        chosen_positions = []
        for i in range(0, self.size // 2):
            chosen_positions += (rotated_grills[0][i, i:self.size - i - 1].tolist())

        # seed(0)
        for order_num, position in enumerate(chosen_positions, 1):
            (i, j) = np.where(position == rotated_grills[randint(0, 3)])
            grille[i, j] = order_num

        return grille


# a = CardanoGrille(5, True)
# print(a.grille)
# print(a.whole_grille())
# print(a.encode('Hello world!'))
# print(a.decode(''))
# print(a.encode('ABCDEFGH'))
# print(a.decode('CDEBAFAHG'))
