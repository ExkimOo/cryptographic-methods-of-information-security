import pytest

from cyphers.scytale_cypher import Scytale


@pytest.mark.parametrize('plaintext, m, cyphertext', [('НАС АТАКУЮТ', '3', 'НАУАТЮСАТ К'),
                                                      ('РАКЕТНЫЕ ВОЙСКА', '3', 'РНОАЫЙКЕСЕ КТВА'),
                                                      ('Hello world', '', None)])
def test_encode(plaintext, m, cyphertext):
    scy = Scytale()
    assert scy.encode(plaintext, m) == cyphertext


@pytest.mark.parametrize('plaintext, m, cyphertext', [('НАУАТЮСАТ К', '3', 'НАС АТАКУЮТ'),
                                                      ('РНОАЫЙКЕСЕ КТВА', '3', 'РАКЕТНЫЕ ВОЙСКА'),
                                                      ('Hello world', '', None)])
def test_decode(plaintext, m, cyphertext):
    scy = Scytale()
    assert scy.decode(plaintext, m) == cyphertext