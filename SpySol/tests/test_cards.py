def test_get_cards():
    from spysol.cards import get_cards, SPADES, HEARTS
    cards = get_cards()
    assert len(cards) == 13 * 8
    assert cards[0].rank == 1
    assert cards[0].index == "A"
    assert cards[0].suit == SPADES
    assert cards[0].name == " A" + SPADES
    assert cards[0].visible
