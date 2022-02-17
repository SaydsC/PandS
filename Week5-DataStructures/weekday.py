# Week 5 task
# Write a program that determines whether today is a weekday or not

# Author: Sadie Concannon
weekDay = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

weekDay = (input("Enter the day of the week: "))

if weekDay == ('Saturday' or 'sunday'):
    print("Yay, its the weekend")
else: print ("Unfortunately it's a weekday")