import random

logo = '''  ________                              ___________.__              _______               ___.                 
 /  _____/ __ __   ____   ______ ______ \__    ___/|  |__   ____    \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/   |    |   |  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  /\  ___/ \___ \ \___ \    |    |   |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  >   |____|   |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/                  \/     \/          \/            \/    \/     \/       
'''

print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

random_number = random.randint(1, 100)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == 'easy':
    tries = 10
elif difficulty == 'hard':
    tries = 5
else:
    while difficulty != 'easy' and difficulty != 'hard':
        difficulty = input("Please type 'easy' or 'hard' to start a game: ")
        if difficulty == 'easy':
            tries = 10
        elif difficulty == 'hard':
            tries = 5

def guess(n, a):
    if n > a:
        print("Too low.\nGuess again.")
    elif n < a:
        print("Too High.\nGuess again.")
    else:
        print(f"You got it! The answer was {n}")

lose = True
cnt = 0
for i in range(tries):
    num = int(input(f"You have {tries - cnt} attempts remaining to guess the number.\nMake a guess: "))
    if random_number != num and i != tries - 1:
        guess(random_number, num)
    
    elif random_number != num and i == tries - 1:
        break

    elif random_number == num:
        guess(random_number, num)
        lose = False
        break

    cnt += 1

if lose == True:
    print("You've run out of guesses, you lose.")