from config import player2
from deck import deck,draw_card
from game import calc_total
import random

def bot_round():
    bot_cards = player2["cards"]
    bot_value = calc_total(bot_cards)

    if bot_value < 17:
        draw_card(deck, bot_cards)
        print(f"{player2['nickname']} dobiera:")
    else:
        player2["choice"] = "pass"
        print(f"{player2['nickname']} passuje")

        