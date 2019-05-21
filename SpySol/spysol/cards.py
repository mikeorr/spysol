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
        try:
            return self.rank == other.rank and self.suit == other.suit
        except AttributeError:
            return NotImplemented

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
        

def get_cards():
    cards = []
    ranks = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
    suits = (SPADES, HEARTS, SPADES, HEARTS, SPADES, HEARTS, SPADES, HEARTS)
    for suit in suits:
        for rank in ranks:
            card = Card(rank, suit)
            cards.append(card)
    return cards

def count_runs(cards):
    runs = 0
    if cards:
        prev = None
        start = None
        for i, card in enumerate(cards):
            if card.is_run(prev):
                if start is None:
                    start = i - 1
            elif start is not None:
                this_run = i - start + 1
                runs.append(this_run)
                start = None
            prev = card
    if start is not None:
        this_run = len(cards) - start + 1
        runs += this_run
    return runs

def is_full_suit(cards):
    if len(cards) < 13:
        return False
    cards = reversed(cards)
    suit = cards[0].suit
    for i in range(12):
        if card[i].rank != i + 1 or card[i].suit != suit:
            return False
    return True
