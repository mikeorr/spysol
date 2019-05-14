import random

import reprutils

SPADES = "\N{BLACK SPADE SUIT}"
HEARTS = "\N{BLACK HEART SUIT}"


class Card(object):
    def __init__(self, rank=1, suit=SPADES):
        self.rank = rank
        self.suit = suit
        self.red = suit == HEARTS
        self.index = self._get_index(rank)
        self.name = f"{self.index:>2s}{self.suit}"

    __repr__ = reprutils.GetattrRepr("rank", "suit")
        
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.formatted_name

    def __eq__(self, other):
        tuple1 = self.rank, self.suit
        try:
            tuple2 = other.rank, other.suit
        except AttributeError:
            return NotImplemented
        return tuple1 == tuple2

    def is_run(self, prev):
        return prev and prev.suit == self.suit and prev.rank == self.rank + 1

    @staticmethod
    def _get_index(rank):
        if rank == 1:
            return "A"
        elif 2 <= rank <= 10:
            return str(rank)
        elif rank == 11:
            return "J"
        elif rank == 12:
            return "Q"
        elif rank == 13:
            return "K"
        else:
            raise ValueError("rank must be between 1 and 13")
        

class Hand(list):
    """A sequence of cards."""

    def count_runs(self):
        runs = 0
        if len(self) > 0:
            prev = self[0]
            for card in self[:1]:
        my_run = 0
        prev = None
        start = None
        for i, card in enumerate(self):
            if card.is_run(prev):
                if start is None:
                    start = i - 1
            elif start is not None:
                my_run = i - 1
                runs += my_run
                start = None

        return runs


class Deck(Hand):
    ranks = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
    suits = (SPADES, HEARTS, SPADES, HEARTS, SPADES, HEARTS, SPADES, HEARTS)

    def __init__(self, cards=None, shuffle=False, random_=None):
        for suit in self.suits:
            for rank in self.ranks:
                card = Card(rank, suit)
                self.cards.append(card)
        self.random = random_ or random
        if shuffle:
            self.shuffle()

    def shuffle(self):
        self.random.shuffle(self)
        

def get_cards():
    cards = []
    ranks = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
    suits = (SPADES, HEARTS, SPADES, HEARTS, SPADES, HEARTS, SPADES, HEARTS)
    for suit in suits:
        for rank in ranks:
            card = Card(rank, suit)
            cards.append(card)
    return cards

def is_run(card1, card2):
    return card1.suit == card2.suit and card1.rank == card2.rank + 1

def is_full_suit(cards):
    if len(cards) < 13:
        return False
    cards = reversed(cards)
    suit = cards[0].suit
    for i in range(12):
        if card[i].rank != i + 1 or card[i].suit != suit:
            return False
    return True

def count_runs(cards):
    runs = 0
    start = None
    stop = None
    prev = None
    for i, card in enumerate(cards):
        if prev:
        else:
            start = i
            stop = i
        prev = card
    return runs
