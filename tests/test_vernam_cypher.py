import pytest

from cyphers.vernam_cypher import Vernam


@pytest.mark.parametrize('plaintext, cyphertext, key', [('', None, ''),
                                                        ('sometext', None, '1'),
                                                        ('KOD', 'æ5ï', '101011010111101010101011'),
                                                        ('KOD', 'æ5ï', '101011010111101010101011101001010101'),
                                                        ('KOD', None, '567'),])
def test_encode(plaintext, cyphertext, key):
    ver = Vernam()
    assert ver.encode(plaintext, key) == cyphertext


@pytest.mark.parametrize('plaintext, cyphertext, key', [('KOD', 'æ5ï', '101011010111101010101011')])
def test_decode(plaintext, cyphertext, key):
    ver = Vernam()
    assert ver.decode(cyphertext, key) == plaintext
