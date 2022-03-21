# author Sadie Concannon
# program that asks the user to input any positive integer and outputs the successive values
# calculate the next value by taking the current value
# when even, divide it by two, 
# when odd, multiply it by three and add one
# end at current value 1

#collatz % modulus

def collatz(number):
    if number % 2==0:
        return number // 2

    elif number % 2 == 1:
        result = 3 * number + 1
        return result
  
n = int(input("Please enter a positive integer: "))
print (n)
while n !=1:
    n = collatz(n)
    print (n)