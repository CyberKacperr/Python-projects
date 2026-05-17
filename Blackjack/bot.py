from config import player2
from deck import deck,draw_card
from game import calc_total
import random

def bot_round():
    bot_value = calc_total(player2["cards"])
    play_chance = random.random()
    if bot_value < 12:
        player2["choice"] = "draw"
        draw_card(deck,player2)
    else:
        player2["choice"] = "pass"
        
        if player2["choice"] == "draw":
            print(f"{player2['nickname']} dobiera \n")
        else:
            print(f"{player2['nickname']} pasuje")

        