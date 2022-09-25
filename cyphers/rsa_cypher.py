from utils.primes import generate_e_d
from utils.basic_algorithms.powmod import powmod


class RSA:
    def encrypt(self, message, e, N, file_in='', file_out=''):
        result = []

        if file_in:
            with open(file_in, 'rb') as file_input, \
                    open(file_out, 'w+') as file_output:
                data = file_input.read()

                for symbol in data:
                    encrypted_block = powmod(symbol, e, N)
                    result.append(str(encrypted_block))

                file_output.write('\n'.join(result))
        else:
            for symbol in message:
                encrypted_block = powmod(ord(symbol), e, N)
                result.append(str(encrypted_block))

            return '\n'.join(result)

    def decrypt(self, message, d, N, file_in='', file_out=''):
        result = []

        if file_in:
            with open(file_in, 'r') as file_input, \
                    open(file_out, 'wb+') as file_output:
                data = file_input.read().split('\n')

                for number in data:
                    decrypted_block = powmod(int(number), d, N)
                    result.append(int.to_bytes(decrypted_block, length=1, byteorder='little'))

                file_output.write(b''.join(result))
        else:
            for symbol in message.split('\n'):
                decrypted_block = powmod(int(symbol), d, N)
                result.append(chr(decrypted_block))

            return ''.join(result)

    def generate_keys(self, p, q):
        e, d = generate_e_d((p - 1) * (q - 1))

        return e, d
