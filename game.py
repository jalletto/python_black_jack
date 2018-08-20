from deck import Deck
import random 
import os

class Game:

    def __init__(self):
        # self.deck = self.make_deck()
        self.deck = Deck()
        self.deck.shuffle()
        self.dealer = []
        self.player = []
        self.deal()
        self.game_over = False

    # def make_deck(self):
    #     deck = []
    #     for suit in self.suits:
    #         deck += [f'A{suit}',f'K{suit}', f'Q{suit}', f'J{suit}' ]
    #         for i in range(2,11):
    #             deck.append(f'{i}{suit}')
    #     return deck 

    def deal(self):
        for _i in range(1,3):
            self.dealer.append(self.deck.deal())
            self.player.append(self.deck.deal())

    def hand_value(self, hand):
        values = list(map(self.card_to_value, hand))
        total = sum(values)
        if total > 21 and 11 in values:
            i = values.index(11)
            values[i] = 1
            return sum(values)
        return total 
    
    def card_to_value(self, card):
        face_cards = ['Q', 'K', 'J', '1']
        card_val = card[0]
        if card_val in face_cards:
            card_val = '10'
        if card_val == 'A':
            card_val = '11'
        return int(card_val)
   
    def can_hit(self, hand):
        return self.hand_value(hand) < 21

    def hit(self, player):
        player.append(self.deck.deal())

    def dealer_play(self):
        while self.hand_value(self.dealer) < 16:
            self.hit(self.dealer)

    def get_winner(self):
        p = self.hand_value(self.player)
        d = self.hand_value(self.dealer)
        if p == 21 or p < 21 and p > d or d > 21:
            self.game_over = True
            print('player wins')
        elif p > 21 or d < 21 and d > p:
            self.game_over = True
            print('dealer wins')
        elif d == p:
            self.game_over = True
            print('tie game.')

    def game_state(self):
        print(f'DEALER')
        self.display_hand(self.dealer)
        print(f'PLAYER Has {self.hand_value(self.player)}\n')
        self.display_hand(self.player)
    
    def display_hand(self, hand):
        cards = []
        for card in hand:
            cards.append(f'| {card} |   ')
        if hand == self.dealer and not self.game_over: 
            cards[0] = '| \\\\ |   '
        print("".join(cards) +' \n')

    
    def play(self):
        self.game_state()
        player_choice = input("S to stay. H to hit.\n").lower()
        while player_choice == "h" and self.can_hit(self.player):
            os.system('clear')
            self.hit(self.player)
            self.game_state()
            player_choice = input("S to stay. H to hit.\n").lower()

        os.system('clear')
        self.dealer_play()
        self.get_winner()
        self.game_state()
