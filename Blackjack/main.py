from os import system
from deck import draw_card
from game import calc_total
from config import player1,player2
from bot import bot_round
round_count = 1

input("""
      Zasady dla tej wersji blackjacka:
      -Walczysz przeciwko dealerowi
      -Jeżeli twoja wartość kart przekroczy 21 to przegrywasz chyba że dealer też przekroczy to jest remis

      Cel gry:
      -Zdobyć 10000zł z portfelu dealera posiadając 1000zł
      -Zwycięstwo z obstawioną kwotą sprawia iż ona wraca do ciebie z podwójną wartością (z portfelu dealera)
      -Minimalna kwota obstawienia -> 100zł
      -jeżeli nie możesz obstawić to automatycznie przegrywasz
      
      Wciśnij enter aby kontynuować...
      """)

player1_nickname = input("Wpisz swoją nazwę użytkonika: ")
player2_nickname = input("Wpisz nazwę przeciwnika: ")

player1["nickname"] = player1_nickname.capitalize()
player2["nickname"] = player2_nickname.capitalize()

for _ in range(2):
    draw_card(player1)
    draw_card(player2)

def round():

    system("cls")
    global round_count
    global player1
    global player2
    game = None
    
    if player1["money"] < 100:
        print("Nie stać cię na obstawienie. Przegrywasz")
        game = "end"

    elif player2["money"] <= 0:
        print("Gratulacje, obrabowałeś dealera. Wygrywasz")
        game = "end"

# end of the round -->

    if game == "end":
        print(f"Ilość rund: {round_count}:")
        print(f"Zwycięstwa: {player1['wins']}")
        print(f"Porażki: {round_count-player1['wins']}")
        exit()

    print(f"Runda: {round_count} ({player1['wins']}:{player2['wins']})")
    print(f"Majątek {player1_nickname} : {player1['money']}")
    print(f"Majątek {player2_nickname} : {player2['money']}")
    round_count+=1


    
    while True:
    
        # bet section -->

        try:    
            bet = int(input("Podaj kwotę do obstawienia (minimum 100zł): "))
            if bet < 100:
                input("Zbyt niska kwota...")
                continue

            elif bet > player1["money"]:
                input("Stary, nawet cie na to nie stać...")
                continue
                
            else: break
        except ValueError:
            print("błąd")
    
    for _ in range(2):
        draw_card(player1)
        draw_card(player2)
    system("cls")
    
    while True:
        
        player1_sum = calc_total(player1["cards"])
        player2_sum = calc_total(player2["cards"])
        # player1['status'] = None

        #Print round info !! -->

        print(f"{player1['cards']} wartość: {player1_sum}")
        print(f"Odkryta karta bota: {player2['cards'][0]}")


        total = calc_total(player1["cards"])

        # draw a card -->

        if player1["choice"] != "pass":
            choice = input("1 - dobierz kartę, 2 - pass \n")

            if choice not in ["1","2"]:
                input("Błąd wpisu. Wciśnij enter aby spróbować ponownie.")
                system("cls")
                continue

            if choice == "1":
                if calc_total(player1["cards"]) < 21:
                    draw_card(player1)
                else:
                    input("Nie możesz już dobierać...")
            else:
                player1["choice"] = "pass"
                input(f"Twój wynik: {total}...")
                system("cls")
        
        if player2["choice"] != "pass":
            bot_round()
        
        # Match result -->

        if player2["choice"] == "pass" and player1["choice"] == "pass":
            system("cls")
            if player1_sum < 21 and player2_sum < 21:
                # player1['status']: True = win, False = loose
                if player1_sum > player2_sum:
                    player1['status'] = True
                    print(f"{player1['nickname']} wygrywa (Przewaga wartości kart).")
                    player1["wins"]+=1

                elif player1_sum < player2_sum:
                    player1['status'] = False
                    print(f"{player2['nickname']} wygrywa (Przewaga wartości kart).")
                    player2["wins"]+=1
            
            elif player1_sum <= 21 and player2_sum > 21:
                    player1['status'] = True
                    print(f"{player1['nickname']} wygrywa (wartość > 21).")
                    player1["wins"]+=1

            elif player1_sum > 21 and player2_sum <= 21:
                    player1['status'] = False
                    print(f"{player2['nickname']} wygrywa (wartość > 21).")
                    player2["wins"]+=1

            else:
                print("Remis")

            if player1['status'] == True:
                player1["money"]+=bet
                player2["money"]-=bet

            elif player1['status'] == False:
                player1["money"]-=bet
                player2["money"]+=bet

        print(player2["choice"] + "\n" + player1["choice"])
        input("Wciśnij enter aby kontynuować")
        system("cls")

        if player1["status"] != None:
            break

def reset(player):
    player["choice"] = ""
    player["cards"] = []
    player['status'] = None

while True:
    reset(player1)
    reset(player2)
    round()