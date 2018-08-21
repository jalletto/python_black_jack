import random

class Deck: 
    suits = [ '\u2663', '\u2666', '\u2660', '\u2665' ]

    def __init__(self):
        self.cards = self.make_deck()

    def make_deck(self):
        deck = []
        for suit in self.suits:
            deck += [f'A{suit}', f'K{suit}', f'Q{suit}', f'J{suit}']
            for i in range(2, 11):
                deck.append(f'{i}{suit}')
        return deck

    def deal(self): 
       return self.cards.pop()

    def len(self):
        return self.cards.len()

    def shuffle(self):
        random.shuffle(self.cards)