# program that asks user to guess a number 
# prompting until they get the right one
# Author: Sadie Concannon

from numpy import integer


numberToGuess = 30
guess = int(input("Please guess the number:"))
while guess != numberToGuess:
    print ("Wrong")
    guess = int(input("Please guess again:"))

print ("Well done Yes the number was ", numberToGuess)
