from game import calc_total
from config import card_value,player1,player2
import random

colors = ["♥", "♦", "♣", "♠"]
values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

deck = [v + c for v in values for c in colors]

def draw_card(hand):
            player_cards = hand["cards"]
            calc_total(player_cards)
            
            card = random.choice(deck)
            player_cards.append(card)
            if hand == player1:
                print(f"Dobierasz: {card} (Wartość: {card_value[card[:-1]]})")
            deck.remove(card)