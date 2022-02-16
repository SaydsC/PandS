#program to tell the user if the number they enter is odd or even
#author Sadie Concannon

number = int(input("enter an integer:"))

if (number % 2) == 0:
    print ("{} is an even number".format (number))
else: 
    print("{} is an odd number".format (number))
    