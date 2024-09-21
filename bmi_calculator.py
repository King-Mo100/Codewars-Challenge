# Get user inputs
height = float(input("What is your height in meters? "))
weight = float(input("What is your weight in kg? "))

# Calculate BMI
bmi = weight / (height ** 2)

# Print the result
print(f"Your BMI is: {round(bmi, 2)}")
