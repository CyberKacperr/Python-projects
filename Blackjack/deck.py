from game import calc_total
from config import card_value
import random

colors = ["H", "D", "C", "S"]
values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

deck = [v + c for v in values for c in colors]

def draw_card(deck,hand):

            card = random.choice(deck)
            print(f"Dobrałeś: {card} (Wartość: {card_value[card[:-1]]})")
            hand.append(card)
            deck.remove(card)