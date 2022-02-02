import numpy as np

from constants import RUS_LETTERS, ENG_LETTERS


class PolybiusSquare():
    def __init__(self):
        self.eng_polybius_square_upper = np.array(list(ENG_LETTERS.translate({ord('J'): None}))).reshape((5, 5))
        self.rus_polybius_square_upper = np.array(list(RUS_LETTERS.translate({ord(i): None for i in 'ЁЙЪ'}))).reshape((5, 6))
        self.eng_polybius_square_lower = np.array(list(ENG_LETTERS.lower().translate({ord('j'): None}))).reshape((5, 5))
        self.rus_polybius_square_lower = np.array(list(RUS_LETTERS.lower().translate({ord(i): None for i in 'ёйъ'}))).reshape(
            (5, 6))

    def encode(self, plaintext):
        cyphertext = []
        for letter in self.__remove_letters(plaintext):
            result = np.array(letter)
            if np.isin(letter, self.eng_polybius_square_upper):
                (i, j) = np.where(self.eng_polybius_square_upper == letter)
                result = self.eng_polybius_square_upper[(i + 1) % 5, j]
            elif np.isin(letter, self.eng_polybius_square_lower):
                (i, j) = np.where(self.eng_polybius_square_lower == letter)
                result = self.eng_polybius_square_lower[(i + 1) % 5, j]
            elif np.isin(letter, self.rus_polybius_square_upper):
                (i, j) = np.where(self.rus_polybius_square_upper == letter)
                result = self.rus_polybius_square_upper[(i + 1) % 5, j]
            elif np.isin(letter, self.rus_polybius_square_lower):
                (i, j) = np.where(self.rus_polybius_square_lower == letter)
                result = self.rus_polybius_square_lower[(i + 1) % 5, j]
            cyphertext += result.tolist()

        return ''.join(cyphertext)

    def decode(self, cyphertext):
        plaintext = []
        for letter in self.__remove_letters(cyphertext):
            result = np.array(letter)
            if np.isin(letter, self.eng_polybius_square_upper):
                (i, j) = np.where(self.eng_polybius_square_upper == letter)
                result = self.eng_polybius_square_upper[(i - 1) % 5, j]
            elif np.isin(letter, self.eng_polybius_square_lower):
                (i, j) = np.where(self.eng_polybius_square_lower == letter)
                result = self.eng_polybius_square_lower[(i - 1) % 5, j]
            elif np.isin(letter, self.rus_polybius_square_upper):
                (i, j) = np.where(self.rus_polybius_square_upper == letter)
                result = self.rus_polybius_square_upper[(i - 1) % 5, j]
            elif np.isin(letter, self.rus_polybius_square_lower):
                (i, j) = np.where(self.rus_polybius_square_lower == letter)
                result = self.rus_polybius_square_lower[(i - 1) % 5, j]
            plaintext += result.tolist()

        return ''.join(plaintext)

    def __remove_letters(self, text):
        return text.translate({ord('J'): 'I', ord('Ё'): 'Е', ord('Й'): 'И', ord('Ъ'): 'Ь'})


a = PolybiusSquare()
print(a.encode('hello HELLO привет ПРИВЕТ'))
print(a.decode('nkqqt NKQQT хцпимш ХЦПИМШ'))
