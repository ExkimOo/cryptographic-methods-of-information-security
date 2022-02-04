import re
from functools import reduce


class Richelieu():
    def encode(self, plaintext, key):
        keys_list = self.__proccess_key(key)
        if keys_list:
            count = 0
            cyphertext = ''
            for keys in keys_list:
                part = plaintext[count + min(keys) - 1:count + max(keys)]
                result = ''.join(part[i - 1] for i in keys)
                cyphertext += result
                count += len(keys)
            cyphertext += plaintext[count:]

            return cyphertext
        return

    def decode(self, cyphertext, key):
        keys_list = self.__proccess_key(key)
        if keys_list:
            count = 0
            plaintext = ''
            for keys in keys_list:
                part = cyphertext[count + min(keys) - 1:count + max(keys)]
                result = ''.join(part[i - 1] for i in keys)
                plaintext += result
                count += len(keys)
            plaintext += cyphertext[count:]

            return plaintext
        return

    def __proccess_key(self, key):
        result = re.findall(r'(\(((\d+,)*\d+)\))', key)
        matches = []
        for patterns in result:
            matches.append(patterns[0])

        patterns_length = len(reduce(lambda x,y: x + y, matches))
        if len(key) != patterns_length:
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

# a = Richelieu()
# print(a.encode('КРИПТОГРАФИЯ', '(3,2,1)(4,2,3,1)(1)(2,1)(2,1)'))
# print(a.decode(a.encode('КРИПТОГРАФИЯ', '(3,2,1)(4,2,3,1)(1)(2,1)(2,1)'), '(3,2,1)(4,2,3,1)(1)(2,1)(2,1)'))