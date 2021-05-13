# This is a number geussing game

import random

print('Hello, what is your name?')
name = input()

print('Well, ' + name + ', I am thinking of a number between 1-20')

secNum = random.randint(1,20)

for guessesTaken in range(1,7):
    print('Take a guess')
    guess = int(input())

    if guess < secNum:
        print('your guess is too low')
    elif guess > secNum:
        print('your guess is too high')
    else:
        break # this is condition for correct guess

if guess == secNum:
    print('Good job, ' + name + '! you guessed my number in ' + str(guessesTaken) + ' guesses')
else:
    print('Nope. the number i was thinking of was ' + str(secNum))

print('You took ' + str(guessesTaken) + ' guesses.')
