import random

#####creation des fonctions
# def pl_win():
#     #end game
#     print(f"You win with {pl_cards_sum} point vs {}")

#1. The user and computer should each get 2 random cards.
def draw_card(nb_card): 
    """ Draw cards.. yes, really"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] #set de depart
    pl_deck = []
    for element in range(nb_card):
        pl_deck.append(random.choice(cards))
    return pl_deck

#2. Add up the user's and the computer's scores
def cards_sum(draw):
    sum = 0
    for card in draw:
        sum += card
    return sum

 #3. Does the user or computer have a blackjack? (ace + 10)
def blackjack_control(pl_cards_pt, cp_cards_pt):
    if pl_cards_pt == 21: #blackjack
        #stop_game
        print("You win with a black jack")
        continue_to_play = False
    elif cp_cards_pt == 21:
        print("You lose, computer has a black jack")
        continue_to_play = False 
    else:
        continue_to_play = True

#4. Is user's score over 21 ?
#5. Do you have an "Ace" ?
def sup21WithAnAce(pl_cards_pt, pl_draw):
    if pl_cards_pt > 21:
        for card in pl_draw:
            if card == 11:
                return True
    
#eleven = sup21WithAnAce(pl_cards_sum)

#6. If the ace counts as a 1 instead of 11, are they still over 21?  !!!!!!!!!!
def aceAsOne_Sup21(pl_cards_pt, is_sup21WithAnAce):
    if is_sup21WithAnAce == True and pl_cards_pt > 21:
        print("You lose")


#7. Ask the user if they want to get another card. Draw another card
def pl_ask_another_card(nb):
    ask_card = input("Do you want to get another card? Type 'y' or 'n': ").lower()
    if ask_card == "y":
        pl_draw.extend(draw_card(nb)) #player now has 3 cards
    return pl_draw

#8. if score is less than 17, keep drawing cards.
# def pl_pointsInf17(pl): # n'est pas utilisé
#     if pl < 17:
#         pl_draw.extend(draw_card(1))
#     return pl_draw

def cp_pointsInf17(cp):
    if cp < 17:
        cp_draw.extend(draw_card(1))
    return cp_draw

def pl_pointsInf17(pl):
    if pl < 17:
        pl_draw.extend(draw_card(1))
    return pl_draw

#9. gone over 21? lose byBurst
def bust(pl, cp):
    if pl > 21:
        print("You lose by bust")
        continue_to_play = False 
    elif cp > 21:       
        print("You win, computer has a bust")
        continue_to_play = False 
    else:
        blackjack_control(pl, cp)


#10. Compare user score with computer score to see if user score is higher?








#continue_to_play = True
# while continue_to_play == True:

#####first draw  
####game
#wanna_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
#1. The user and computer should each get 2 random cards.
#2. Add up the user's and the computer's scores

pl_draw = draw_card(2) 
pl_total_points = cards_sum(pl_draw)
print(f"Your cards : {pl_draw}, current score: {pl_total_points}")

cp_draw = draw_card(2)
cp_total_points = cards_sum(cp_draw)
print(f"Computer's first card is {cp_draw[0]} {cp_draw[1]} ")

#3. Does the user or computer have a blackjack? (ace + 10)
blackjack_control(pl_total_points, cp_total_points)

#4. Is user's score over 21 ? #5. Do you have an "Ace" ?
is_sup21WithAnAce = sup21WithAnAce(pl_total_points, pl_draw)

#6. If the ace counts as a 1 instead of 11, are they still over 21?
aceAsOne_Sup21(pl_total_points, is_sup21WithAnAce)

#7. Ask the user if they want to get another card. Draw another card
pl_pointsInf17(pl_total_points)
pl_total_points = cards_sum(pl_draw)
print(f"Your cards : {pl_draw}, current score: {pl_total_points}")
instantFail = bust(pl_total_points, cp_total_points)
pl_ask_another_card(1)


#8. Computer plays, if score is less than 17, keep drawing cards.
cp_pointsInf17(cp_total_points)
cp_total_points = cards_sum(cp_draw)
print(cp_total_points)

#9. Has computer gone over 21? Burst
instantFail = bust(pl_total_points, cp_total_points)



#9. gone over 21?
