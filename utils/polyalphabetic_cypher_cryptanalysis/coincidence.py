# -*- coding: cp1251 -*-
import re
from collections import Counter

import numpy as np

from constants.constants import RUS_LETTERS, ENG_LETTERS

threshold = {'ENG': 0.054, 'RUS': 0.055}


class Coincidence:
    def get_key(self, text, lang):
        alphabet = RUS_LETTERS.lower() if lang == 'RUS' else ENG_LETTERS.lower()
        text = re.sub(r'[^а-яё]', '', text.lower()) if lang == 'RUS' else re.sub(r'[^a-z]', '', text.lower())
        try:
            key_length = self.__find_key_length(text, lang)
        except:
            print('Проверенные длины ключа от 2 до 15 не перешли порог ожидаемого индекса совпадений')
            return
        lines = self.__split_text(text, key_length)
        shifts = self.__find_shifts(lines, alphabet, lang)
        print(shifts)

        possible_keys = [''.join([alphabet[(-number + i) % len(alphabet)] for number in shifts]) for i in range(len(alphabet))]

        return possible_keys

    def __find_key_length(self, text, lang):
        key_length = []
        for t in range(2, 15):
            lines = self.__split_text(text, t)
            values = np.array(list(self.__coincidence_index(line) for line in lines))
            print(values)
            if np.all(values > threshold[lang]):
                key_length.append(t)

        return key_length[0]

    def __split_text(self, text, t):
        lines = []
        for i in range(t):
            letters_list = []
            for j in range(i, len(text), t):
                letters_list.append(text[j])

            lines.append(''.join(letters_list))

        return lines

    def __find_shifts(self, lines, alphabet, lang):
        all_coeffs = []
        for i in range(1, len(lines)):
            coeffs = []
            for shift in range(1, len(alphabet) + 1):
                coeffs.append(self.__count_mutual_coincidence_index(lines[0], lines[i], shift, lang, alphabet))
            all_coeffs.append(coeffs)

        shifts = list(np.argmax(np.array(all_coeffs), axis=1) + 1)
        shifts.insert(0, 0)

        return shifts

    def __coincidence_index(self, string):
        counter = Counter(string)

        n = sum(counter.values())
        index = 0

        for f in counter.values():
            index += f * (f - 1) / (n * (n - 1))

        return index

    def __count_mutual_coincidence_index(self, string1, string2, shift, lang, alphabet):
        counter1 = Counter(string1)
        counter2 = Counter(string2)

        for letter in alphabet:
            if letter not in counter1.keys():
                counter1[letter] = 0
            if letter not in counter2.keys():
                counter2[letter] = 0

        counter1 = sorted(counter1.items(), key=lambda x: x[0])
        counter2 = sorted(counter2.items(), key=lambda x: x[0])

        if lang == 'RUS':
            counter1.insert(6, counter1[-1])
            counter2.insert(6, counter2[-1])

        counter1 = dict(counter1)
        counter2 = dict(counter2)

        n1 = sum(counter1.values())
        n2 = sum(counter2.values())
        mutual_index = 0

        for f, g in zip(counter1.values(), list(counter2.values())[-shift:] + list(counter2.values())[:-shift]):
            mutual_index += f * g / (n1 * n2)

        return mutual_index