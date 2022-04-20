# -*- coding: cp1251 -*-
import re
from math import gcd
from collections import Counter

class Kasiski:
    def find_key_length(self, text):
        text = re.sub(r'[^A-ZА-ЯЁ]', '', text.upper())
        patterns_distances = self.__count_distances(text)
        patterns_lengths = self.__delete_odd_lengths(Counter(map(lambda x: gcd(*x), patterns_distances)))

        return patterns_lengths.most_common(1)[0][0]

    def __count_distances(self, text):
        patterns_distances = []
        for i in range(len(text) - 3):
            indexes = [m.start(0) for m in re.finditer(text[i:i + 3], text)]
            if len(indexes) >= 3:
                patterns_distances.append([indexes[i + 1] - indexes[i] for i in range(len(indexes) - 1)])

        return patterns_distances

    def __delete_odd_lengths(self, patterns_lengths):
        lengths_to_delete = []
        for key in patterns_lengths.keys():
            if key in (1, 2) or key > 20:
                lengths_to_delete.append(key)

        for length in lengths_to_delete:
            patterns_lengths.pop(length)

        return patterns_lengths