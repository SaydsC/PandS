# author Sadie Concannon
# Task Week 7, Write a program that reads in a text file and outputs the number of e's it contains. 
# Think about what is being asked here, document any assumptions you are making.
# The program should take the filename from an argument on the command line. 

# open file using lab , filename as a variable and to first read text file
#above from lab, now to output only the number of e's
    # try cheat sheet count method
filename = 'TheDreamOfTheReveller.txt'
with open(filename, "r") as f:
    data = f.read()
    print(data)
def letterFrequency(filename, letter):
# open file in read mode
    file = open(filename, "r")
# content of file as a variable
    text = file.read()
# use count from cheat sheet
    return text.count(letter)
# functions and specify the letter e
print (letterFrequency(filename, 'e'))

    