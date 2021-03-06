import bitarray
from bitarray.util import ba2int, int2ba

S = [[0xF, 0xC, 0x2, 0xA, 0x6, 0x4, 0x5, 0x0, 0x7, 0x9, 0xE, 0xD, 0x1, 0xB, 0x8, 0x3],
     [0xB, 0x6, 0x3, 0x4, 0xC, 0xF, 0xE, 0x2, 0x7, 0xD, 0x8, 0x0, 0x5, 0xA, 0x9, 0x1],
     [0x1, 0xC, 0xB, 0x0, 0xF, 0xE, 0x6, 0x5, 0xA, 0xD, 0x4, 0x8, 0x9, 0x3, 0x7, 0x2],
     [0x1, 0x5, 0xE, 0xC, 0xA, 0x7, 0x0, 0xD, 0x6, 0x2, 0xB, 0x4, 0x9, 0x3, 0xF, 0x8],
     [0x0, 0xC, 0x8, 0x9, 0xD, 0x2, 0xA, 0xB, 0x7, 0x3, 0x6, 0x5, 0x4, 0xE, 0xF, 0x1],
     [0x8, 0x0, 0xF, 0x3, 0x2, 0x5, 0xE, 0xB, 0x1, 0xA, 0x4, 0x7, 0xC, 0x9, 0xD, 0x6],
     [0x3, 0x0, 0x6, 0xF, 0x1, 0xE, 0x9, 0x2, 0xD, 0x8, 0xC, 0x4, 0xB, 0xA, 0x5, 0x7],
     [0x1, 0xA, 0x6, 0x8, 0xF, 0xB, 0x0, 0x4, 0xC, 0x3, 0x5, 0x9, 0x7, 0xD, 0x2, 0xE]]


class GOST:
    def encrypt(self, text, key):
        return self.__enc_dec(text, key, 'enc')

    def decrypt(self, text, key):
        return self.__enc_dec(text, key, 'dec')

    def __enc_dec(self, text, key, mode):
        keys = self.__generate_keys(key)

        N1, N2 = text[:32], text[32:]

        key_indexes = list(range(8)) * 3 + list(range(7, -1, -1))
        rounds_indexes = range(32)

        if mode == 'dec':
            rounds_indexes = reversed(rounds_indexes)

        for round in rounds_indexes:
            N1, N2 = self.__func_F(N1, keys[key_indexes[round]], round) ^ N2, N1

        return N2 + N1

    def __generate_keys(self, key):
        keys = []
        for i in range(0, 256, 32):
            keys.append(key[i:i + 32])

        return keys

    def __func_F(self, N2, key, round):
        text = int2ba((ba2int(N2) + ba2int(key)) % 2 ** 32, length=32)

        text_S = bitarray.bitarray()
        for i in range(0, 32, 4):
            text_S += int2ba(S[round % 8][ba2int(text[i:i + 4])], length=4)

        return text_S[11:] + text_S[:11]

    def ECB(self, text, key, mode):
        text = self.__expand_text_len(text)
        key = self.__expand_key_len(key)

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
        text = self.__expand_text_len(text)
        key = self.__expand_key_len(key)
        init_vect_text = self.__expand_key_len(init_vect_text)

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
        text = self.__expand_text_len(text)
        key = self.__expand_key_len(key)
        init_vect_text = self.__expand_key_len(init_vect_text)

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
        text = self.__expand_text_len(text)
        key = self.__expand_key_len(key)
        init_vect_text = self.__expand_key_len(init_vect_text)

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

    def __expand_text_len(self, text):
        if len(text) % 8 != 0:
            text += ' ' * (8 - len(text) % 8)

        return text

    def __expand_key_len(self, key):
        if len(key) == 0:
            return 'this_is_a_pasw_for_GOST_28147_89'

        if len(key) % 32 != 0:
            key += ' ' * (32 - len(key) % 32)

        return key

    def __expand_init_vect_len(self, init_vect):
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
        key_bin.frombytes(key[:32].encode('koi8-r'))

        return key_bin

    def __init_vect_to_bin(self, init_vect):
        init_vect_bin = bitarray.bitarray()
        init_vect_bin.frombytes(init_vect[:8].encode('koi8-r'))

        return init_vect_bin