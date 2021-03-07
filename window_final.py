import random
import sys
import os
from PyQt5 import QtGui, QtWidgets, QtCore, uic
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QApplication, QMainWindow, QPushButton


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.flipped = False

    def flip(self):
        # flip function flipped our card when we need it
        self.flipped = not self.flipped

    def show(self):
        return "{}_of_{}".format(self.value, self.suit)

    # Implementing build in methods so that you can print a card object
    def __str__(self):
        return self.show()

    def __repr__(self):
        return self.show()


class Deck(QtWidgets.QMainWindow):
    def __init__(self, values, suits, parent=None):
        self.cards = []
        self.create_deck(values, suits)
        self.shuffle()

        super(Deck, self).__init__(parent)

        self.mover = 80
        self.win = QMainWindow()
        self.win.setGeometry(0, 0, 1920, 1080)
        self.win.setWindowTitle('Solitaire')

        button = QPushButton('Show cards', self.win)
        button.setObjectName('btn')
        button.setToolTip('This is a button')
        button.move(20, 20)

        for i in self.cards:
            label = QtWidgets.QLabel(self.win)
            label.setText('123')
            label.move(self.mover, self.mover)
            label.setObjectName(f'label{i}')
            label.resize(600, 800)
            self.mover += 3

            pixmap = QtGui.QPixmap(os.path.join(r'Solitaire\png_cards',
                                                f'{i}.png'))
            label.setPixmap(pixmap)

        button.clicked.connect(self.label_image)
        self.win.show()

    def label_image(self):
        pass
        # for i in self.cards:
            # label = QtWidgets.QLabel(self.win)
            # label.setText('123')
            # label.move(self.mover, self.mover)
            # label.setObjectName(f'label{i}')
            # label.resize(500, 726)
            # self.mover += 5
            # pixmap = QtGui.QPixmap(os.path.join(r'\Solitaire\png_cards',
            #                                     f'{i}.png'))
            # self.win.label[i].setPixmap(pixmap)

        self.show()


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
        if len(self.cards) > 0:
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


class Board(QtWidgets.QMainWindow):
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    suits = {'hearts', 'diamonds', 'clubs', 'spades'}

    piles_num = 7  # number of Piles

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Board, cls).__new__(cls)
        return cls.instance

    def __init__(self, parent=None):
        self.deck = Deck(self.values, self.suits)
        self.piles = []

        super(Board, self).__init__(parent)

        self.ui = uic.loadUi("solitaire_gui.ui")
        self.ui.Btn_image.clicked.connect(self.label_image)

        self.ui.show()

    def label_image(self):
        # pixmap = QtGui.QPixmap('2_of_hearts.png')

        value = ['2', '3']
        suit = ['hearts', 'diamonds']
        mover = 100

        # self.labels = dict()

        for v in value:
            for s in suit:
                # name = f'label_{v}_{s}'
                # label = QtWidgets.QLabel()
                # label.setObjectName(name)
                # self.ui.addWidget(label)
                # self.labels[name] = label

                # label = QtWidgets.QLabel()
                # setattr(self, f'label_{v}_{s}', label)
                pixmap = QtGui.QPixmap(os.path.join(r'png_cards', f'{v}_of_{s}.png'))
                self.ui.label_card.setPixmap(pixmap)
                # label.move(mover, mover)
                # label.resize(10, 10)

    def get_game_elements(self):
        gge_object = {
            "deck": str(self.deck),
            "piles": [str(pile) for pile in self.piles]
        }

        return gge_object


if __name__ == '__main__':
    values = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']
    suits = {'hearts', 'diamonds', 'clubs', 'spades'}
    app = QtWidgets.QApplication(sys.argv)
    window = Deck(values, suits)
    window.create_deck(values, suits)
    sys.exit(app.exec())



