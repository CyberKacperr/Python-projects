import os
from deck import deck,draw_card
from game import calc_total
from config import player1,player2
from bot import bot_round

player1_nickname = input("Wpisz swoją nazwę użytkonika: ")
opponent_nickname = input("Wpisz nazwę przeciwnika: ")

player1["nickname"] = player1_nickname.capitalize()
player2["nickname"] = opponent_nickname.capitalize()

for _ in range(2):
    draw_card(deck,player1)
    draw_card(deck,player2)

def round(i = 0):
    global player1
    os.system("cls")
    i+=1
    while True:
        player1_sum = calc_total(player1["cards"])
        player2_sum = calc_total(player2["cards"])
        print(player1["cards"])
        print(player1_sum)

        total = calc_total(player1["cards"])
        choice = input("1 - dobierz kartę, 2 - pass \n")

        if choice not in ["1","2"]:
            input("Błąd wpisu. Wciśnij enter aby spróbować ponownie.")
            os.system("cls")
            continue
        choice = int(choice)

        message = "Wciśnij enter aby kontynuować"
        match choice:
            case 1:
                if calc_total(player1["cards"]) < 21:
                    draw_card(deck,player1)
                else:
                    message = "Nie możesz już dobierać. Wciśnij enter aby kontynuować"
            case 2:
                player1["choice"] = "pass"
                print(f"Twój wynik: {total}")
        
        if player2["choice"] == "":
            bot_round()
            continue
        
        if player2["choice"] == player1["choice"] == "pass":
            if player1_sum < player2_sum:
                print(f"{player1['nickname']} wygrywa.")
            elif player1_sum < player2_sum:
                f"{player2['nickname']} wygrywa."
            else: print("Remis")


        input(message)
        os.system("cls")

round()