"""
Function to guess the number from user
"""
import random
NUMBER = random.randint(1, 10)

PLAYER_NAME = input("Hello, what is your name? ")
NUMBER_OF_GUESSES = 0
print(f'I\'m glad to meet you! {PLAYER_NAME} \nLet\'s play a game with you, I will think a number between 1 and 10 then you will guess, alright? \nDon\'t forget! You have only 3 chances so guess:')

while NUMBER_OF_GUESSES < 3:
    GUESS = int(input())
    NUMBER_OF_GUESSES += 1
    if GUESS < NUMBER:
        print('Your estimate is too low, go up a little!')
    if GUESS > NUMBER:
        print('Your estimate is too high, go down a bit!')
    if GUESS == NUMBER:
        break
if GUESS == NUMBER:
    print(f"Congratulations {PLAYER_NAME}, you guessed the number in {NUMBER_OF_GUESSES} tries!")
else:
    print(f'Close but no cigar, you couldn\'t guess the number. \nWell, the number was {NUMBER}.')
