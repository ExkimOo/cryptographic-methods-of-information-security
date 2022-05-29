import bitarray
from bitarray.util import ba2int, int2ba

from constants.constants import pc_1, pc_2, E, S, P, IP, FP, shifts


class DES:
    def encrypt(self, text, key):
        return self.__enc_dec(text, key, 'enc')

    def decrypt(self, text, key):
        return self.__enc_dec(text, key, 'dec')

    def __enc_dec(self, text, key, mode):
        keys = self.__key_expansion(key)
        text_ip = self.__text_initial_permutation(text)

        N1, N2 = text_ip[:32], text_ip[32:]

        indexes = range(16) if mode == 'enc' else range(15, -1, -1)

        for round in indexes:
            N1, N2 = N2, self.__func_F(N2, keys[round]) ^ N1

        return self.__text_final_permutation(N2 + N1)

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

    def ECB(self, text, key, mode):
        text = self.expand_text_len(text)
        key = self.expand_key_len(key)

        text_bin = self.__text_to_bin(text)
        key_bin = self.__key_to_bin(key)

        enc_dec_text = []

        if mode == 'enc':
            for i in range(0, len(text_bin), 64):
                enc_dec_text.append(self.encrypt(text_bin[i:i + 64], key_bin).tobytes().decode('koi8-r'))

        if mode == 'dec':
            for i in range(0, len(text_bin), 64):
                enc_dec_text.append(self.decrypt(text_bin[i:i + 64], key_bin).tobytes().decode('koi8-r'))

        return ''.join(enc_dec_text)

    def CBC(self, text, key, init_vect_text, mode):
        text = self.expand_text_len(text)
        key = self.expand_key_len(key)
        init_vect_text = self.expand_key_len(init_vect_text)

        text_bin = self.__text_to_bin(text)
        key_bin = self.__key_to_bin(key)
        vect = self.__init_vect_to_bin(init_vect_text)

        enc_dec_text = []

        if mode == 'enc':
            for i in range(0, len(text_bin), 64):
                vect = self.encrypt(text_bin[i:i + 64] ^ vect, key_bin)
                enc_dec_text.append(vect.tobytes().decode('koi8-r'))

        if mode == 'dec':
            for i in range(0, len(text_bin), 64):
                enc_dec_text.append((vect ^ self.decrypt(text_bin[i:i + 64], key_bin)).tobytes().decode('koi8-r'))
                vect = text_bin[i:i + 64]

        return ''.join(enc_dec_text)

    def CFB(self, text, key, init_vect_text, mode):
        text = self.expand_text_len(text)
        key = self.expand_key_len(key)
        init_vect_text = self.expand_key_len(init_vect_text)

        text_bin = self.__text_to_bin(text)
        key_bin = self.__key_to_bin(key)
        vect = self.__init_vect_to_bin(init_vect_text)

        enc_dec_text = []

        if mode == 'enc':
            for i in range(0, len(text_bin), 64):
                vect = self.encrypt(vect, key_bin) ^ text_bin[i:i + 64]
                enc_dec_text.append(vect.tobytes().decode('koi8-r'))

        if mode == 'dec':
            for i in range(0, len(text_bin), 64):
                enc_dec_text.append((self.encrypt(vect, key_bin) ^ text_bin[i:i + 64]).tobytes().decode('koi8-r'))
                vect = text_bin[i:i + 64]

        return ''.join(enc_dec_text)

    def OFB(self, text, key, init_vect_text, mode):
        text = self.expand_text_len(text)
        key = self.expand_key_len(key)
        init_vect_text = self.expand_key_len(init_vect_text)

        text_bin = self.__text_to_bin(text)
        key_bin = self.__key_to_bin(key)
        vect = self.__init_vect_to_bin(init_vect_text)

        enc_dec_text = []

        if mode == 'enc':
            for i in range(0, len(text_bin), 64):
                vect = self.encrypt(vect, key_bin)
                enc_dec_text.append((vect ^ text_bin[i:i + 64]).tobytes().decode('koi8-r'))

        if mode == 'dec':
            for i in range(0, len(text_bin), 64):
                vect = self.encrypt(vect, key_bin)
                enc_dec_text.append((vect ^ text_bin[i:i + 64]).tobytes().decode('koi8-r'))

        return ''.join(enc_dec_text)

    def expand_text_len(self, text):
        if len(text) % 8 != 0:
            text += ' ' * (8 - len(text) % 8)

        return text

    def expand_key_len(self, key):
        if len(key) == 0:
            return 'DESkey56'

        if len(key) % 32 != 0:
            key += ' ' * (32 - len(key) % 32)

        return key

    def expand_init_vect_len(self, init_vect):
        if len(init_vect) == 0:
            return 'abcdefgh'

        if len(init_vect) % 8 != 0:
            init_vect += ' ' * (8 - len(init_vect) % 8)

        return init_vect

    def __text_to_bin(self, text):
        text_bin = bitarray.bitarray()
        text_bin.frombytes(text.encode('koi8-r'))

        return text_bin

    def __key_to_bin(self, key):
        key_bin = bitarray.bitarray()
        key_bin.frombytes(key[:8].encode('koi8-r'))

        return key_bin

    def __init_vect_to_bin(self, init_vect):
        init_vect_bin = bitarray.bitarray()
        init_vect_bin.frombytes(init_vect[:8].encode('koi8-r'))

        return init_vect_bin