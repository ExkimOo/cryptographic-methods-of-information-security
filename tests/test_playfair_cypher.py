import pytest

from cyphers.playfair_cypher import Playfair


@pytest.mark.parametrize('lang, key, plaintext, cyphertext', [('ENG', '', '', None),
                                                              ('ENG', 'WHEATSON', 'IDIOCYOFTENLOOKSLIKEINTELLIGENCE',
                                                               'KFFBBZFMWASPNVCFDUKDAGCEWPQDPNBSNE'),
                                                              ('ENG', 'WHEATSON', 'IDIOCYOFTENLOOKSLIKEINTELLIGENCES',
                                                              'KFFBBZFMWASPNVCFDUKDAGCEWPQDPNBSWN'),])
def test_encode(lang, key, plaintext, cyphertext):
    pl = Playfair(lang, key)
    assert pl.encode(plaintext) == cyphertext


@pytest.mark.parametrize('lang, key, plaintext, cyphertext', [('ENG', '', None, '')])
def test_decode(lang, key, plaintext, cyphertext):
    pl = Playfair(lang, key)
    assert pl.decode(cyphertext) == plaintext