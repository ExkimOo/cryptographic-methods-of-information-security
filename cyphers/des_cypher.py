import bitarray
from bitarray.util import ba2int, int2ba, ba2hex, hex2ba

from constants.constants import pc_1, pc_2, E, S, P, IP, FP, shifts


class DES:
    def encrypt(self, text, key):
        return self.__enc_dec(text, key, 'enc')

    def decrypt(self, text, key):
        return self.__enc_dec(text, key, 'dec')

    def __enc_dec(self, text, key, mode):
        key_bin = bitarray.bitarray()
        key_bin.frombytes(key.encode('utf-8')[:64])
        if len(key_bin) < 64:
            print('Short key')
            return

        text_bin = bitarray.bitarray()
        if mode == 'enc':
            text_bin.frombytes(text.encode('utf-8'))
        else:
            text_bin = hex2ba(text)

        if (length := len(text_bin) % 64) != 0:
            text_bin += (64 - length) * bitarray.bitarray('0')

        keys = self.__key_expansion(key_bin)

        result = bitarray.bitarray()
        for i in range(0, len(text_bin), 64):
            text_ip = self.__text_initial_permutation(text_bin[i:i + 64])

            N1 = text_ip[:32]
            N2 = text_ip[32:]

            indexes = range(16) if mode == 'enc' else range(15, -1, -1)

            for round in indexes:
                N1, N2 = N2, self.__func_F(N2, keys[round]) ^ N1

            N1, N2 = N2, N1
            encrypted_text_bin = N1 + N2

            result += self.__text_final_permutation(encrypted_text_bin)

        if mode == 'dec':
            try:
                return result.tobytes().decode('utf-8')
            except:
                print('Error encoding to utf-8')
                return
        else:
            return ba2hex(result)

    def __key_expansion(self, key):
        key_pc1 = bitarray.bitarray()
        for i in range(8):
            for j in range(7):
                key_pc1.append(key[pc_1[i][j] - 1])

        key_left = key_pc1[:28]
        key_right = key_pc1[28:]

        keys_left_shifted = []
        keys_right_shifted = []
        for shift in shifts:
            key_left = key_left[shift:] + key_left[:shift]
            keys_left_shifted.append(key_left)

            key_right = key_right[shift:] + key_right[:shift]
            keys_right_shifted.append(key_right)

        keys_pc2 = []
        for i in range(16):
            left_right = keys_left_shifted[i] + keys_right_shifted[i]

            tmp = bitarray.bitarray()
            for i in range(8):
                for j in range(6):
                    tmp.append(left_right[pc_2[i][j] - 1])

            keys_pc2.append(tmp)

        return keys_pc2

    def __text_initial_permutation(self, text):
        text_ip = bitarray.bitarray()
        for i in range(8):
            for j in range(8):
                text_ip.append(text[IP[i][j] - 1])

        return text_ip

    def __text_final_permutation(self, text):
        encrypted_text_fp = bitarray.bitarray()
        for i in range(8):
            for j in range(8):
                encrypted_text_fp.append(text[FP[i][j] - 1])

        return encrypted_text_fp

    def __expansion_permutation(self, R):
        R_expansed = bitarray.bitarray()
        for i in range(8):
            for j in range(6):
                R_expansed.append(R[E[i][j] - 1])

        return R_expansed

    def __substitutions(self, res):
        res_s = bitarray.bitarray()
        for i in range(0, 48, 6):
            row = ba2int(bitarray.bitarray([res[i], res[i + 5]]))
            col = ba2int(res[i + 1:i + 5])

            res_s += int2ba(S[i // 6][row][col], length=4)

        return res_s

    def __permutation(self, res_s):
        res_s_f = bitarray.bitarray()
        for i in range(8):
            for j in range(4):
                res_s_f.append(res_s[P[i][j] - 1])

        return res_s_f

    def __func_F(self, N2, key):
        R_expansed = self.__expansion_permutation(N2)
        res = key ^ R_expansed
        res_s = self.__substitutions(res)
        res_s_f = self.__permutation(res_s)

        return res_s_f