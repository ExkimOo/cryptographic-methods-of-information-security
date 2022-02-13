import re
from functools import reduce


class Richelieu():
    def encode(self, plaintext, key):
        return self.__enc_dec(plaintext, key)

    def decode(self, cyphertext, key):
        return self.__enc_dec(cyphertext, key)

    def __enc_dec(self, text, key):
        keys_list = self.__proccess_key(key)
        if keys_list:
            count = 0
            enc_dec_text = ''
            for keys in keys_list:
                part = text[count + min(keys) - 1:count + max(keys)]
                result = ''.join(part[i - 1] for i in keys)
                enc_dec_text += result
                count += len(keys)
            enc_dec_text += text[count:]

            return enc_dec_text
        return

    def __proccess_key(self, key):
        result = re.findall(r'(\(((\d+,)*\d+)\))', key)
        matches = []
        for patterns in result:
            matches.append(patterns[0])

        if len(matches) == 0: return

        patterns_len = len(reduce(lambda x,y: x + y, matches))
        if len(key) != patterns_len:
            print('Строка введена неверно')
            return

        result = []
        for pattern in matches:
            numbers = list(map(int, re.findall(r'(\d+)', pattern)))
            if max(numbers) - min(numbers) + 1 != len(numbers):
                print('Ошибка ключа')
                return

            result.append(numbers)

        return result

a = Richelieu()
print(a.encode('КРИПТОГРАФИЯ', '(3,2,1)(4,2,3,1)(1)(2,1)(2,1)'))
print(a.decode(a.encode('КРИПТОГРАФИЯ', '(3,2,1)(4,2,3,1)(1)(2,1)(2,1)'), '(3,2,1)(4,2,3,1)(1)(2,1)(2,1)'))