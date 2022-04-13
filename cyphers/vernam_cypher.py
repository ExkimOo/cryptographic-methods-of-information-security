import sys


class Vernam():
    def encode(self, plaintext, key):
        return self.__enc_dec(plaintext, key)

    def decode(self, cyphertext, key):
        return self.__enc_dec(cyphertext, key)

    def __enc_dec(self, text, key):
        if len(key) > len(text):
            key = key[:len(text)]

        try:
            koi_text = text.encode('koi8-r', 'strict')
        except:
            print('Текст содержит недопустимые символы (КОИ-8)')
            return

        try:
            koi_key = key.encode('koi8-r', 'strict')
        except:
            print('Ключ содержит недопустимые символы (КОИ-8)')
            return

        # if bytes('\r') in koi_text:
        #     print('Ban')
        print('Text:', koi_text)
        print('Key:', koi_key)

        byte_text = int.from_bytes(koi_text, byteorder=sys.byteorder)
        print('Byte text:', byte_text)
        byte_key = int.from_bytes(koi_key, byteorder=sys.byteorder)
        print('Byte key:', byte_key)
        print('Encoded:', (byte_text ^ byte_key).to_bytes(len(text), byteorder=sys.byteorder))
        print('Encoded:', (byte_text ^ byte_key))
        enc_dec_text = (byte_text ^ byte_key).to_bytes(len(text), byteorder=sys.byteorder).decode('koi8-r')
        print(enc_dec_text)
        # print()

        return enc_dec_text