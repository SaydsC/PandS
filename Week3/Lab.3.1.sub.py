#program that reads out two numbers
#and can subtract one from the other
#Author: Sadie Concannon

#input reads in a string so we need to convert it into an int
#so we can perform mathematical operations

x = int(input ("Enter first number: "))
y = int(input ("Enter second number: "))
answer = x-y
print("{} minus {} is {} ".format(x, y, answer))
