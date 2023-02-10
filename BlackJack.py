import random
import os
import time

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


status = {
    0 : 'default',
    1 : 'You win 😃',
    2 : 'You lose 😤',
    3 : 'Opponent went over. You win 😁',
    4 : 'You went over. You lose 😭',
    5 : 'Win with a Blackjack 😎',
    6 : 'Lose, opponent has Blackjack 😱',
    7 : 'Draw 🙃'
}

def black_jack(your_card, dealer_card, more_card):
    a = sum(your_card)
    b = sum(dealer_card)
    if a < 21 and b < 21 and more_card == False:
        if a > b:
            game_status = 1
        elif a == b:
            game_status = 7
        else :
            game_status = 2
    elif a < 21 and b < 21 and more_card == True:
        game_status = 0
    elif a == 21 and b == 21:
        game_status = 2
    elif a != 21 and b == 21:
        game_status = 6
    elif a == 21 and b != 21:
        game_status = 5
    elif a > 21 and b > 21:
        if 11 in your_card and 11 in dealer_card:
            your_card[your_card.index(11)] -= 10
            dealer_card[dealer_card.index(11)] -= 10
            black_jack(your_card, dealer_card, more_card)
        elif 11 in your_card and 11 not in dealer_card:
            your_card[your_card.index(11)] -= 10
            game_status = 3
        elif 11 in dealer_card and 11 not in your_card:
            dealer_card[dealer_card.index(11)] -= 10
            game_status = 4
        else:
            game_status = 4
            
    return game_status


def game_start(start):
    if start == 'y':
        game_status = 0 
        more_card = True
        print(logo)
        your_card = random.choices(cards, k = 2)
        dealer_card = random.choices(cards, k = 2)
        print(f'\n    Your cards: {your_card}, current score: {sum(your_card)}')
        print(f"    Computer's first card: {dealer_card[0]}")
        time.sleep(1)

        while game_status == 0:
            if black_jack(your_card, dealer_card, more_card) != 0:
                print(f'\n    Your final hands: {your_card}, final score: {sum(your_card)}')
                print(f"    Computer's final hand: {dealer_card}, final score: {sum(dealer_card)}\n")
                print(status[black_jack(your_card, dealer_card, more_card)])
                break
            get_card = input("\nType 'y' to get another card, type 'n' to pass: ").lower()
            
            if get_card == 'y':
                your_card.append(random.choice(cards))
                dealer_card.append(random.choice(cards))
            
            elif get_card == 'n':
                more_card = False
                print(f'\n    Your final hands: {your_card}, final score: {sum(your_card)}')
                print(f"    Computer's final hand: {dealer_card}, final score: {sum(dealer_card)}\n")
                print(status[black_jack(your_card, dealer_card, more_card)])
                break
            
                
        again = input("\n Do you want to play again? Type 'y' or 'n': ").lower()
        if again == 'y':
            game_start(again)

    elif start == 'n':
        return 0

    else:
        start = input("\nPlease type in 'y' or 'n' to proceed the game: ").lower()
        os.system('cls')
        game_start(start)
    

game_start(start)