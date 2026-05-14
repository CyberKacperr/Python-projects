from config import card_value

def calc_total(cards):
    total = 0
    ace = 0

    for c in cards:
        value = c[:-1]
        total += card_value[value]

        if value == "A":
            ace+=1
    
    while total > 21 and ace:
        total-=10
        ace-=1

    return total
