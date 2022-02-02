import numpy as np

from random import randint, seed


class CardanoGrille():
    def __init__(self, size=6, jumbled=True):
        self.size = size
        self.grille = self.__generate_grille()
        self.jumbled = jumbled

    def encode(self, plaintext):
        cyphertext = []
        plaintext_matrix = np.array(list(plaintext)).reshape((self.size, self.size))
        print(plaintext_matrix)
        if self.jumbled:
            pass
        else:
            for rotation in range(4):
                num_of_posiitons = int(np.max(self.grille))
                result = []
                for position in range(1, num_of_posiitons + 1):
                    (i, j) = np.where(position == np.rot90(self.grille, k=-rotation))
                    result += plaintext_matrix[i, j].tolist()
                cyphertext += result

        return ''.join(cyphertext)

    def __generate_grille(self):
        grill = np.zeros((self.size, self.size))
        rotated_grills = [
            np.arange(self.size ** 2).reshape((self.size, self.size)),
            np.rot90(np.arange(self.size ** 2).reshape((self.size, self.size)), k=-1),
            np.rot90(np.arange(self.size ** 2).reshape((self.size, self.size)), k=-2),
            np.rot90(np.arange(self.size ** 2).reshape((self.size, self.size)), k=-3)
        ]

        chosen_positions = []
        for i in range(0, self.size // 2):
            chosen_positions += (rotated_grills[0][i, i:self.size - i - 1].tolist())

        seed(0)
        for order_num, position in enumerate(chosen_positions, 1):
            (i, j) = np.where(position == rotated_grills[randint(0, 3)])
            grill[i, j] = order_num

        return grill


a = CardanoGrille(4, False)
print(a.grille)
print(a.encode('ABCDEFGHIJKLMNOP'))
