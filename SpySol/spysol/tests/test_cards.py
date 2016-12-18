import spysol.cards as sc

def test_card():
    card = sc.Card(sc.RANKS[0], sc.HEARTS)
    assert card.rank == (1, "A")
    assert card.suit == sc.HEARTS
    assert card.color == sc.RED
    assert card.is_red is True
    assert card.is_black is False

def test_deck():
    deck = sc.Deck()
    assert len(deck) == 52
    card1 = deck[0]
    card2 = sc.Card(sc.RANKS[0], sc.SPADES)
    card3 = sc.Card(sc.RANKS[1], sc.SPADES)
    card4 = sc.Card(sc.RANKS[0], sc.CLUBS)
    assert card1.rank == card2.rank
    assert card1.suit == card2.suit
    assert card1 == card2
    assert card1 != card3
    assert card1 != card4
    assert card1.rank.level == card3.rank.level - 1
    assert deck.suits == {sc.SPADES, sc.CLUBS, sc.DIAMONDS, sc.HEARTS}

def test_spider_deck():
    deck = sc.Deck(suits=2, decks=2)
    assert len(deck) == 52 * 2
    assert deck.suits == {sc.SPADES, sc.HEARTS}
