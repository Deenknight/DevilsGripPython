import random


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.flipped = False

    def flip(self):
        # flip function flipped our card when we need it
        self.flipped = not self.flipped

    def show(self):
        return "{} of {} | flipped = {}".format(self.value, self.suit, self.flipped)

    # Implementing build in methods so that you can print a card object
    def __str__(self):
        return self.show()

    def __repr__(self):
        return self.show()


class Deck:
    def __init__(self, values, suits):
        self.cards = []
        self.create_deck(values, suits)
        self.shuffle()


    # Generate 52 cards
    def create_deck(self, values, suits):
        self.cards = []
        for suit in suits:
            for val in values:
                self.cards.append(Card(val, suit))

    # Display all cards in the deck
    def show(self):
        for card in self.cards:
            print(card.show())

    def shuffle(self):
        random.shuffle(self.cards)

    def get_first_card(self):
        if len(self.cards) > 0:
            return self.cards[0]
        else:
            return None

    def take_first_card(self, flip=True):
        if len(self.cards) > 0:
            nextCard = self.cards.pop(0)
            if flip and len(self.cards) > 0:
                self.cards[0].flip()
            return nextCard
        else:
            return None

    def draw_card(self):
        if len(self.cards)>0:
            self.cards[0].flip()
            self.cards.append(self.cards.pop(0))
            self.cards[0].flip()

    def __str__(self):
        return "{}".format(self.cards)


class Pile:
    def __init__(self):
        self.cards = []

    def addCard(self, card):
        self.cards.insert(0, card)

    def flipFirstCard(self):
        if len(self.cards) > 0:
            self.cards[0].flip(self)

    def getFlippedCards(self):
        return [card for card in self.cards if card.flipped]

    def __str__(self):
        return f'Cards: {self.cards}'


class Board:
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    suits = {'hearts', 'diamonds', 'clubs', 'spades'}

    piles_num = 7  # number of Piles

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Board, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.deck = Deck(self.values, self.suits)
        self.piles = []

    def get_game_elements(self):
        gge_object = {
            "deck": str(self.deck),
            "piles": [str(pile) for pile in self.piles]
        }

        return gge_object


