# program to guess the number
#with hint too high too low
#Author: Sadie Concannon

import random

numberToGuess = random.randint(1,100)

guess = int(input("Please guess the number:"))
while guess != numberToGuess:
    if guess < numberToGuess:
        print ("Too Low")
    else: #I know it cant be equal or too low, so it must be too high
        print ("Too High")
    guess = int(input("Please Guess Again:"))
if guess == numberToGuess:
    
    print("Well Done, Yes the number was ", numberToGuess)
    