import os
from deck import deck,draw_card
from game import calc_total
from config import player1,player2
from bot import bot_round

round_count = 1

input("""
      Zasady dla tej wersji blackjacka:
      -Walczysz przeciwko dealerowi
      -Jeżeli twoja wartość kart przekroczy 21 to przegrywasz chyba że dealer też przekroczy to jest remis
      -Znasz tylko swoje karty
      
      Wciśnij enter aby kontynuować...
      """)

player1_nickname = input("Wpisz swoją nazwę użytkonika: ")
opponent_nickname = input("Wpisz nazwę przeciwnika: ")

player1["nickname"] = player1_nickname.capitalize()
player2["nickname"] = opponent_nickname.capitalize()

# Do zrobienia:
# Gracz dostaje 1000zł na start
# Dealer dostaje 10000zł na start
# Wpisujesz swoją kwotę do obstawienia:
# Jeśli wygrasz: Odbierasz dealerowi obstawioną przez ciebie kwotę
# Jeśli przegrasz: Oddajesz dealerowi obstawioną przez ciebie kwotę
# Minimalna wartość do obstawienia: 100zł
# Jeśli przejmiesz cały majątek dealera to wygrywasz (W przypadku bankructwa przegrywasz)
# 

for _ in range(2):
    draw_card(deck,player1)
    draw_card(deck,player2)

def round():
    os.system("cls")
    round_status = "start"

    global round_count
    global player1
    global player2
    
    message = "Wciśnij enter aby kontynuować"
    input(f"Runda: {round_count} ({player1['wins']}:{player2['wins']})")
    round_count+=1
    for _ in range(2):
        draw_card(deck,player1)
        draw_card(deck,player2)
    os.system("cls")
    
    while True:
        
        player1_sum = calc_total(player1["cards"])
        player2_sum = calc_total(player2["cards"])
        print(f"{player1['cards']} wartość: {player1_sum}")


        total = calc_total(player1["cards"])

        if player1["choice"] != "pass":
            choice = input("1 - dobierz kartę, 2 - pass \n")


        if choice not in ["1","2"]:
            input("Błąd wpisu. Wciśnij enter aby spróbować ponownie.")
            os.system("cls")
            continue

        match choice:
            case "1":
                if calc_total(player1["cards"]) < 20:
                    draw_card(deck,player1)
                else:
                    message = "Nie możesz już dobierać..."
            case "2":
                player1["choice"] = "pass"
                print(f"Twój wynik: {total}")
        
        if player2["choice"] != "pass":
            bot_round()
        
        if player2["choice"] == "pass" and player1["choice"] == "pass":
            round_status = "end"
            if player1_sum < 21 and player2_sum < 21:

                if player1_sum > player2_sum:
                    print(f"{player1['nickname']} wygrywa (Przewaga wartości kart).")
                    player1["wins"]+=1

                elif player1_sum < player2_sum:
                    print(f"{player1['nickname']} wygrywa (Przewaga wartości kart).")
                    player2["wins"]+=1
            
            elif player1_sum < 21 and player2_sum > 21:
                    print(f"{player1['nickname']} wygrywa (wartość > 21).")
                    player1["wins"]+=1

            elif player1_sum > 21 and player2_sum < 21:
                    print(f"{player1['nickname']} wygrywa (wartość > 21).")
                    player2["wins"]+=1

            else: print("Remis")


        input(message)
        os.system("cls")
        
        if round_status == "end":
            break

def reset(player):
    player["choice"] = ""
    player["cards"] = []

while True:
    reset(player1)
    reset(player2)
    round()