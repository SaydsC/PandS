# program to calculate a persons Body Mass Index BMI
# Author: Sadie Concannon
# BMI = weight/height*height
# weight in KG and Height in meters, bmi is weight divided by height squared

def BMI(height, weight):
    bmi=weight/(height**2)
    return bmi
# Defining variables and assign values
height = 1.80
weight = 65
# calculate the BMI function using variables 
bmi = BMI (height, weight)
print("The BMI is", format(round(bmi,2)), "therefore ", end='')
# conditions to find out BMI category use if functions
if (bmi < 18.5) :
    print("Underweight")
elif ( bmi >= 18.5 and bmi < 24.9) :
    print("Healthy")
elif ( bmi >= 24.9 and bmi < 30) :
    print("Overweight")
elif ( bmi >=30) :
    print("Suffering from Obesity")
# amend BMI to 2 decimal places added round to bmi format
