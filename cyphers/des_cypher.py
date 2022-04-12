pc_1 = [[57, 49, 41, 33, 25, 17, 9],
        [1, 58, 50, 42, 34, 26, 18],
        [10, 2, 59, 51, 43, 35, 27],
        [19, 11, 3, 60, 52, 44, 36],
        [63, 55, 47, 39, 31, 23, 15],
        [7, 62, 54, 46, 38, 30, 22],
        [14, 6, 61, 53, 45, 37, 29],
        [21, 13, 5, 28, 20, 12, 4]]

pc_2 = [[14, 17, 11, 24, 1, 5],
        [3, 28, 15, 6, 21, 10],
        [23, 19, 12, 4, 26, 8],
        [16, 7, 27, 20, 13, 2],
        [41, 52, 31, 37, 47, 55],
        [30, 40, 51, 45, 33, 48],
        [44, 49, 39, 56, 34, 53],
        [46, 42, 50, 36, 29, 32]]

E = [[32, 1, 2, 3, 4, 5],
     [4, 5, 6, 7, 8, 9],
     [8, 9, 10, 11, 12, 13],
     [12, 13, 14, 15, 16, 17],
     [16, 17, 18, 19, 20, 21],
     [20, 21, 22, 23, 24, 25],
     [24, 25, 26, 27, 28, 29],
     [28, 29, 30, 31, 32, 1]]

S = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
      [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
      [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
      [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
     [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
      [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
      [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
      [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],
     [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
      [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
      [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
      [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 15]],
     [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
      [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
      [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
      [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],
     [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
      [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
      [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
      [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],
     [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
      [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
      [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
      [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],
     [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
      [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
      [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
      [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
     [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
      [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
      [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
      [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]

P = [[16, 7, 20, 21],
     [29, 12, 28, 17],
     [1, 15, 23, 26],
     [5, 18, 31, 10],
     [2, 8, 24, 14],
     [32, 27, 3, 9],
     [19, 13, 30, 6],
     [22, 11, 4, 25]]

IP = [[58, 50, 42, 34, 26, 18, 10, 2],
      [60, 52, 44, 36, 28, 20, 12, 4],
      [62, 54, 46, 38, 30, 22, 14, 6],
      [64, 56, 48, 40, 32, 24, 16, 8],
      [57, 49, 41, 33, 25, 17, 9, 1],
      [59, 51, 43, 35, 27, 19, 11, 3],
      [61, 53, 45, 37, 29, 21, 13, 5],
      [63, 55, 47, 39, 31, 23, 15, 7]]

FP = [[40, 8, 48, 16, 56, 24, 64, 32],
      [39, 7, 47, 15, 55, 23, 63, 31],
      [38, 6, 46, 14, 54, 22, 62, 30],
      [37, 5, 45, 13, 53, 21, 61, 29],
      [36, 4, 44, 12, 52, 20, 60, 28],
      [35, 3, 43, 11, 51, 19, 59, 27],
      [34, 2, 42, 10, 50, 18, 58, 26],
      [33, 1, 41, 9, 49, 17, 57, 25]]

shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

import bitarray
from bitarray.util import ba2int, int2ba, ba2hex


class DES:
    def encrypt(self, text, key):
        return self.__enc_dec(text, key, 'enc')

    def decrypt(self, text, key):
        return self.__enc_dec(text, key, 'dec')

    def __enc_dec(self, text, key, mode):
        # text = text.encode('utf-16')
        # key = key.encode('utf-16')

        text_bin = bitarray.bitarray()
        text_bin.frombytes(text)
        # text_bin = bitarray.bitarray('0000 0001 0010 0011 0100 0101 0110 0111 1000 1001 1010 1011 1100 1101 1110 1111')
        # text_bin = bitarray.bitarray('1000 0111 1000 0111 1000 0111 1000 0111 1000 0111 1000 0111 1000 0111 1000 0111')
        # text_bin = bitarray.bitarray('0001001000110100010101101010101111001101000100110010010100110110')
        print('Text bin:', text_bin)

        key_bin = bitarray.bitarray()
        key_bin.frombytes(key)
        # key_bin = bitarray.bitarray('00010011 00110100 01010111 01111001 10011011 10111100 11011111 11110001')
        # key_bin = bitarray.bitarray('0000 1110 0011 0010 1001 0010 0011 0010 1110 1010 0110 1101 0000 1101 0111 0011')
        # key_bin = bitarray.bitarray('1010101010111011000010010001100000100111001101101100110011011101')
        print('Key bin:', key_bin)

        keys = self.__key_expansion(key_bin)
        text_ip = self.__text_initial_permutation(text_bin)

        N1 = text_ip[:32]
        N2 = text_ip[32:]

        indexes = range(16) if mode == 'enc' else range(15, -1, -1)

        for round in indexes:
            N1, N2 = N2, self.__func_F(N2, keys[round]) ^ N1
            # print(ba2hex(N1), ba2hex(N2), ba2hex(keys[round]))

        N1, N2 = N2, N1
        encrypted_text_bin = N1 + N2

        encrypted_text_fp = self.__text_final_permutation(encrypted_text_bin)

        print('Encrypted:', encrypted_text_fp)
        print(ba2hex(encrypted_text_fp))
        print(encrypted_text_fp.tobytes().decode('utf-16'))

        return encrypted_text_fp

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


a = DES()
a.encrypt('АБВГ'.encode('utf-8'), 'аылг'.encode('utf-8'))
print()
a.decrypt('潟₻䉮ℷ'.encode('utf-8'), 'аылг'.encode('utf-8'))