import pytest

from cyphers.atbash_cypher import Atbash

@pytest.mark.parametrize('plaintext, cyphertext', [('hello HELLO привет ПРИВЕТ', 'svool SVOOL поцэъм ПОЦЭЪМ'),
                                                   ('', '')])
def test_encode(plaintext, cyphertext):
    atb = Atbash()
    assert atb.encode(plaintext) == cyphertext


@pytest.mark.parametrize('plaintext, cyphertext', [('svool SVOOL поцэъм ПОЦЭЪМ', 'hello HELLO привет ПРИВЕТ')])
def test_decode(plaintext, cyphertext):
    atb = Atbash()
    assert atb.decode(cyphertext) == plaintext