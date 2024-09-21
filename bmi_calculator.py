# Get user inputs
height = float(input("What is your height in meters? "))
weight = float(input("What is your weight in kg? "))

# Calculate BMI
bmi = weight / (height ** 2)

# Print the result
print(f"Your BMI is: {round(bmi, 2)}")

#Codewars challenge

def bmi(weight, height):
    #your code here
    bmi= weight/(height**2)
    
    if bmi <= 18.5:
        return "Underweight"

    elif bmi <= 25.0:
        return "Normal"

    elif bmi <= 30.0:
        return "Overweight"

    elif bmi > 30:
        return "Obese"

# fucntion call example
print(bmi(70, 1.75))