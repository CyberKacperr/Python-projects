import os
from deck import deck,draw_card
from game import calc_total
player1_cards = []

for _ in range(2):
    draw_card(deck,player1_cards)

def round(i = 0):
    os.system("cls")
    i+=1
    while True:
        sum = calc_total(player1_cards)
        print(player1_cards)
        print(sum)

        total = calc_total(player1_cards)
        choice = input("1 - dobierz kartę, 2 - pass \n")

        if choice not in ["1","2"]:
            input("Błąd wpisu. Wciśnij enter aby spróbować ponownie.")
            os.system("cls")
            continue
        choice = int(choice)

        message = "Wciśnij enter aby kontynuować"
        match choice:
            case 1:
                if calc_total(player1_cards) < 21:
                    draw_card(deck,player1_cards)
                else:
                    message = "Nie możesz już dobierać. Wciśnij enter aby kontynuować"
            case 2:
                print(f"Twój wynik: {total}")
        input(message)
        os.system("cls")

round()