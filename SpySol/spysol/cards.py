import collections

RED = "Red"
BLACK = "Black"

SPADES = "\N{BLACK SPADE SUIT}"
CLUBS = "\N{BLACK CLUB SUIT}"
DIAMONDS = "\N{BLACK DIAMOND SUIT}"
HEARTS = "\N{BLACK HEART SUIT}"

SUITS = (SPADES, CLUBS, DIAMONDS, HEARTS)
RED_SUITS = (DIAMONDS, HEARTS)
COLORS = (RED, BLACK)

Rank = collections.namedtuple("Rank", "level name")

RANKS = (
    Rank(1, "A"), Rank(2, "2"), Rank(3, "3"), Rank(4, "4"), Rank(5, "5"),
    Rank(6, "6"), Rank(7, "7"), Rank(8, "8"), Rank(9, "9"), Rank(10, "10"),
    Rank(11, "J"), Rank(12, "Q"), Rank(13, "K"),
    )


class Card(object):
    def __init__(self, rank, suit):
        assert rank in RANKS
        assert suit in SUITS
        self.rank = rank
        self.suit = suit
        self.color = suit in RED_SUITS and RED or BLACK
        self.is_red = self.color is RED
        self.is_black = not self.is_red
        self.formatted_name = "{:>2s}{}".format(rank.name, suit)
        
    def __str__(self):
        return self.formatted_name

    def __repr__(self):
        return self.formatted_name
        #classname = self.__class__.__name__
        #return "{}({}, {})".format(classname, self.rank, self.suit)

    def __eq__(self, other):
        tuple1 = self.rank, self.suit
        try:
            tuple2 = other.rank, other.suit
        except AttributeError:
            return NotImplemented
        return tuple1 == tuple2
        
        

class Deck(list):
    def __init__(self, suits=4, decks=1, *, original=None):
        if original is not None:
            self.original = original
        else:
            self.original = self.make_original(num_suits=suits, num_decks=decks)
        self.reset()

    def reset(self):
        self[:] = self.original
        self.suits = set(x.suit for x in self)

    @staticmethod
    def make_original(num_suits, num_decks):
        if num_suits == 4:
            suits = (SPADES, CLUBS, DIAMONDS, HEARTS)
        elif num_suits == 2:
            suits = (SPADES, SPADES, HEARTS, HEARTS)
        elif suits == 1:
            suits = (SPADES, SPADES, SPADES, SPADES)
        else:
            raise ValueError("arg 'suits'` must be 1, 2, or 4")
        cards = []
        for deck in range(num_decks):
            for suit in suits:
                for rank in RANKS:
                    card = Card(rank, suit)
                    cards.append(card)
        return tuple(cards)
