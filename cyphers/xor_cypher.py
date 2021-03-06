import sys

from utils.prng.lcg import lcg, set_seed


class XOR():
    def encode(self, plaintext, seed):
        return self.__enc_dec(plaintext, seed)

    def decode(self, cyphertext, seed):
        return self.__enc_dec(cyphertext, seed)

    def __enc_dec(self, text, seed):
        set_seed(seed)

        enc_dec_text = ''
        for letter in text.encode('koi8-r'):
            key = lcg()
            enc_dec_text += (letter ^ key).to_bytes(1, byteorder=sys.byteorder).decode('koi8-r')

        return enc_dec_text