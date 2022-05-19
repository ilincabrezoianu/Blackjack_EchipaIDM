import random
from constants import *

#definim clasa Deck - unde stau cartile inainte de a fi impartite pentru joc
class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for value in RANKS:
            for suit in SUITS:
                self.cards.append((value, suit)) # adaugam cartile in lista
    
    def shuffle(self):
        random.shuffle(self.cards) #shuffle-uim lista de carti

    def deal(self):
        if len(self.cards) > 1:
            return self.cards.pop()

#definim clasa Hand care reprezinta mana jucatorului
class Hand(Deck):
    def __init__(self):
        self.cards = []
        self.card_img = []
        self.value = 0 #valoarea cartilor din mana
    
    def add_card(self, card):
        self.cards.append(card)
    
    def calc_hand(self): #calculam pe baza regulilor valoarea mainii
        first_card_index = [a_card[0] for a_card in self.cards]
        non_aces = [c for c in first_card_index if c != 'A']
        aces = [c for c in first_card_index if c == 'A']

        for card in non_aces:
            if card in 'JQK':
                self.value += 10
            else:
                self.value += int(card)
        
        for card in aces:
            if self.value <= 10:
                self.value += 11
            else:
                self.value += 1
        
    def display_cards(self):
        for card in self.cards:
            cards = "".join((card[0], card[1]))
            if cards not in self.card_img:
                self.card_img.append(cards)