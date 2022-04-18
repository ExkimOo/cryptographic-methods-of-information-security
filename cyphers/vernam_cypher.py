import bitarray


class Vernam():
    def encode(self, plaintext, key):
        return self.__enc_dec(plaintext, key)

    def decode(self, cyphertext, key):
        return self.__enc_dec(cyphertext, key)

    def __enc_dec(self, text, key):
        if text == '':
            return

        if len(key) < len(text):
            print('Короткий ключ')
            return

        text_bin = bitarray.bitarray()
        text_bin.frombytes(text.encode('koi8-r'))

        key_bin = bitarray.bitarray()
        key_bin.frombytes(key[:len(text)].encode('koi8-r'))

        return (text_bin ^ key_bin).tobytes().decode('koi8-r')