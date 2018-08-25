from deck import Deck
from player import Player
import os

class Game:

    def __init__(self):
        self.game_over = False
        self.deck = Deck()
        self.dealer = Player()
        self.player = Player()
        self.deck.shuffle()
        self.deal()

    def deal(self):
        for _i in range(1,3):
            self.dealer.hand.append(self.deck.deal())
            self.player.hand.append(self.deck.deal())
   
    def can_hit(self, player):
        return player.hand_total()  < 21

    def hit(self, player):
        player.hand.append(self.deck.deal())

    def dealer_play(self):
        while self.dealer.hand_total() < 16:
            self.hit(self.dealer)

    def get_winner(self):
        player = self.player.hand_total()
        dealer = self.dealer.hand_total()
        if player == 21 or player < 21 and player > dealer or dealer > 21:
            self.game_over = True
            print('player wins')
        elif player > 21 or dealer < 21 and d > player:
            self.game_over = True
            print('dealer wins')
        elif dealer == player:
            self.game_over = True
            print('tie game.')

    def game_state(self):
        print(f'DEALER')
        self.display_hand(self.dealer.hand)
        print(f'PLAYER Has {self.player.hand_total()}\n')
        self.display_hand(self.player.hand)
    
    def display_hand(self, hand):
        cards = []
        for card in hand:
            cards.append(str(card))
        if hand == self.dealer.hand and not self.game_over: 
            cards[0] = card.card_back
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
