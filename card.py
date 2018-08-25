class Card: 

    card_back = '| \\\\ |'
    def __init__(self, suit, value, face=None):
        self.suit = suit
        self.face = face  
        self.value = value 

    def __str__(self):
        return f'| { self.face if self.face else self.value }{self.suit}  | '
