from config import player2
from deck import draw_card
from game import calc_total
import random

def bot_round():
    bot_value = calc_total(player2["cards"])

    if bot_value < 17:
        player2["choice"] = "draw"
        draw_card(player2)
        print(f"{player2['nickname']} dobiera \n")

    else:
        player2["choice"] = "pass"
        print(f"{player2['nickname']} pasuje")