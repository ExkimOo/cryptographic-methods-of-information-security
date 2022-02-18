import pytest

from cyphers.hill_cypher import Hill


ENG = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ .?'

@pytest.mark.parametrize('key, plaintext, cyphertext, alphabet', [('KEKW', 'EGOR', 'G.FV', ENG)])
def test_encode(key, plaintext, cyphertext, alphabet):
    hill = Hill(key, alphabet)
    assert hill.encode(plaintext) == cyphertext


@pytest.mark.parametrize('key, plaintext, cyphertext, alphabet', [('KEKW', 'EGOR', 'G.FV', ENG)])
def test_decode(key, plaintext, cyphertext, alphabet):
    hill = Hill(key, alphabet)
    assert hill.decode(cyphertext).rstrip() == plaintext