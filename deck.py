import random
from card import Card

class Deck: 
    suits = [ '\u2663', '\u2666', '\u2660', '\u2665' ]

    def __init__(self):
        self.cards = self.make_deck()

    def make_deck(self):
        deck = []
        for suit in self.suits:
            deck += [Card(suit, 11, 'A'), Card(suit, 10, 'K'),
                     Card(suit, 10, 'Q'), Card(suit, 10, 'J')]
            # deck += [f'A{suit}', f'K{suit}', f'Q{suit}', f'J{suit}']
            for i in range(2, 11):
                deck.append(Card(suit, i ))
        return deck

    def deal(self): 
       return self.cards.pop()

   

    def shuffle(self):
        random.shuffle(self.cards)

