from game import calc_total
from config import card_value,player1
import random

colors = ["♥", "♦", "♣", "♠"]
values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

deck = [v + c for v in values for c in colors]

def draw_card(deck,hand):
            # print(hand)
            print(hand)
            player_cards = hand["cards"]
            player_nickname = hand["nickname"]
            
            card = random.choice(deck)
            print(f"{player_nickname} dobrał: {card} (Wartość: {card_value[card[:-1]]})")
            player_cards.append(card)
            deck.remove(card)
        
        # jeśli nie ma kart - error