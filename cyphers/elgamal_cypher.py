from utils.basic_algorithms.powmod import powmod

from random import randint


class ElGamal:
    def encrypt(self, message, g, d, p, file_in='', file_out=''):
        result = []

        if file_in:
            with open(file_in, 'rb') as file_input, \
                    open(file_out, 'w+') as file_output:
                data = file_input.read()

                for symbol in data:
                    k = randint(p // 10, p - 3)

                    r = powmod(g, k, p)
                    e = (symbol * powmod(d, k, p)) % p
                    file_output.write(str(r) + ' ' + str(e) + '\n')

                file_output.write('\n'.join(result))
        else:
            for symbol in message:
                k = randint(p // 10, p - 3)

                r = powmod(g, k, p)
                e = (ord(symbol) * powmod(d, k, p)) % p
                result.append((str(r) + ' ' + str(e) + '\n'))

            return ''.join(result)[:-1]

    def decrypt(self, message, c, p, file_in='', file_out=''):
        result = []

        if file_in:
            with open(file_in, 'r') as file_input, \
                    open(file_out, 'wb+') as file_output:
                data = file_input.read().split('\n')[:-1]

                for number in data:
                    r, e = number.split(' ')
                    decrypted_block = (powmod(int(r), p - 1 - c, p) * int(e)) % p
                    result.append(int.to_bytes(decrypted_block, length=1, byteorder='little'))

                file_output.write(b''.join(result))
        else:
            for symbol in message.split('\n'):
                r, e = symbol.split(' ')
                decrypted_block = (powmod(int(r), p - 1 - c, p) * int(e)) % p
                result.append(chr(decrypted_block))

            return ''.join(result)


# a = ElGamal()
# print(a.encrypt('123', 5, 366, 503))
# print(a.decrypt('''60 196
# 60 200
# 60 204''', 160, 503))
# a.encrypt('', 5, 366, 503,
#                 r"C:\Users\Egor\Desktop\123.txt",
#                 r"C:\Users\Egor\Desktop\321.txt")
# a.decrypt('', 160, 503,
#                 r"C:\Users\Egor\Desktop\321.txt",
#                 r"C:\Users\Egor\Desktop\12345.txt")
