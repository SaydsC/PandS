# program to calculate a persons Body Mass Index BMI
# Author: Sadie Concannon
# BMI = weight/height*height
# weight in KG and Height in meters

def BMI(height, weight):
    bmi=weight/(height**2)
    return bmi
# Driver Code
height = 1.8
weight = 65
# calling the BMI function
bmi = BMI (height, weight)
print("The BMI is", format(bmi), "so ", end='')
# conditions to find out BMI category
if (bmi < 18.5) :
    print("Underweight")
elif ( bmi >= 18.5 and bmi < 24.9) :
    print("Healthy")
elif ( bmi >= 24.9 and bmi < 30) :
    print("Overweight")
elif ( bmi >=30) :
    print("Suffering from Obesity")
