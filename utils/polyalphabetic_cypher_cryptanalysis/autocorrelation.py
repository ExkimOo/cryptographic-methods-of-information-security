import re
from collections import Counter

from scipy.stats import chisquare
import numpy as np

from constants.constants import RUS_LETTERS, ENG_LETTERS

exp_freq = {
    'RUS': {'а': 0.0800, 'б': 0.0159, 'в': 0.0454, 'г': 0.0170, 'д': 0.0298, 'е': 0.0845, 'ё': 0.0004, 'ж': 0.0094,
            'з': 0.0165, 'и': 0.0735, 'й': 0.0121, 'к': 0.0349, 'л': 0.0440, 'м': 0.0321, 'н': 0.0670, 'о': 0.1097,
            'п': 0.0281, 'р': 0.0473, 'с': 0.0547, 'т': 0.0626, 'у': 0.0262, 'ф': 0.0026, 'х': 0.0097, 'ц': 0.0048,
            'ч': 0.0144, 'ш': 0.0073, 'щ': 0.0036, 'ъ': 0.0004, 'ы': 0.0190, 'ь': 0.0174, 'э': 0.0032, 'ю': 0.0064,
            'я': 0.0201},
    'ENG': {'A': 0.0805, 'B': 0.0154, 'C': 0.0306, 'D': 0.0399, 'E': 0.1251, 'F': 0.0230, 'G': 0.0196,
            'H': 0.0549, 'I': 0.0726, 'J': 0.0016, 'K': 0.0067, 'L': 0.0414, 'M': 0.0253, 'N': 0.0709,
            'O': 0.0760, 'P': 0.0200, 'Q': 0.0011, 'R': 0.0612, 'S': 0.0654, 'T': 0.0925, 'U': 0.0271,
            'V': 0.0099, 'W': 0.0192, 'X': 0.0019, 'Y': 0.0173, 'Z': 0.0009}
}


class Autocorrelation:
    def get_key(self, text, lang):
        text = re.sub(r'[^а-яё]', '', text.lower()) if lang == 'RUS' else re.sub(r'[^a-z]', '', text.lower())
        alphabet = RUS_LETTERS.lower() if lang == 'RUS' else ENG_LETTERS.lower()

        sigmas = self.__count_sigmas(text)
        key_length = self.__find_key_length(sigmas)
        lines = self.__split_text(text, key_length)
        statistics = self.__count_statistics(lines, alphabet, lang, key_length)
        key = self.__find_key(statistics, alphabet)

        return key

    def __count_sigmas(self, text):
        sigmas = []
        text_len = len(text)
        for t in range(1, len(text[:400])):
            n = 0
            for remained_text, shifted_remained_text in zip(text[t:], text[:-t]):
                if remained_text == shifted_remained_text:
                    n += 1
            sigmas.append(n / (text_len - t))

        return sigmas

    def __find_key_length(self, sigmas):
        periodic_t = [i for i in range(len(sigmas)) if sigmas[i] > 0.05]
        distances = [periodic_t[i + 1] - periodic_t[i] for i in range(len(periodic_t) - 1)]
        key_length = Counter(distances).most_common(1)[0][0]

        return key_length

    def __split_text(self, text, t):
        lines = []
        for i in range(t):
            letters_list = []
            for j in range(i, len(text), t):
                letters_list.append(text[j])

            lines.append(''.join(letters_list))

        return lines

    def __count_statistics(self, lines, alphabet, lang, key_length):
        statistics = []
        for i in range(key_length):
            counter = Counter(lines[i])

            for letter in alphabet:
                if letter not in counter.keys():
                    counter[letter] = 0

            counter = sorted(counter.items(), key=lambda x: x[0])

            if lang == 'RUS':
                counter.insert(6, counter[-1])

            counter = dict(counter)

            line_len = len(lines[i])
            freqs = [count / line_len for count in counter.values()]

            stat = []
            for shift in range(len(alphabet)):
                expected = list(exp_freq[lang].values())
                shifted = freqs[shift:] + freqs[:shift]

                for i in range(len(shifted)):
                    shifted[i] += 0.1
                    expected[i] += 0.1

                stat.append(chisquare(np.array(expected) * 100, np.array(shifted) * 100).statistic)

            statistics.append(stat)

        return statistics

    def __find_key(self, statistics, alphabet):
        key = []
        for arr in statistics:
            key.append(alphabet[np.argmin(arr)])

        return ''.join(key)