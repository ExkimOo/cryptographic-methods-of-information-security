import pytest

from cyphers.richelieu_cypher import Richelieu


@pytest.mark.parametrize('plaintext, cyphertext, key', [('CRYPTOGRAPHY', None, ''),
                                                        ('CRYPTOGRAPHY', None, '('),
                                                        ('CRYPTOGRAPHY', None, '()'),
                                                        ('CRYPTOGRAPHY', None, '(0)'),
                                                        ('CRYPTOGRAPHY', None, '(2)'),
                                                        ('CRYPTOGRAPHY', None, '(1,,'),
                                                        ('CRYPTOGRAPHY', None, '30'),
                                                        ('CRYPTOGRAPHY', None, '(1,2)(0)'),
                                                        ('CRYPTOGRAPHY', None, '(1,2)(2)'),
                                                        ('CRYPTOGRAPHY', None, '(0,1,2)'),
                                                        ('CRYPTOGRAPHY', None, '(13,1,2,3,4,5,6,7,8,9,10,11,12)'),
                                                        ('CRYPTOGRAPHY', None, '(1,3,2,4,5)(1,2,3,4,5,6,7,8,9)'), ])
def test_encode(plaintext, cyphertext, key):
    rich = Richelieu()
    assert rich.encode(plaintext, key) == cyphertext


@pytest.mark.parametrize('plaintext, cyphertext, key', [(None, '', '')])
def test_decode(plaintext, cyphertext, key):
    rich = Richelieu()
    assert rich.decode(cyphertext, key) == plaintext