import reprutils

SPADES = "\N{BLACK SPADE SUIT}"
CLUBS = "\N{BLACK CLUB SUIT}"
DIAMONDS = "\N{BLACK DIAMOND SUIT}"
HEARTS = "\N{BLACK HEART SUIT}"


class Card(object):
    def __init__(self, rank=1, red=False, visible=True):
        self.rank = rank
        self.red = red
        self.visible = visible
        self.index = self._get_index(rank)
        self.suit = red and HEARTS or SPADES
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
        

def get_cards(visible=True):
    cards = []
    ranks = list(range(1, 13+1))
    reds = [False, True, False, True, False, True, False, True]
    for red in reds:
        for rank in ranks:
            card = Card(rank, red, visible)
            cards.append(card)
    return cards
