# Get user inputs
height = float(input("What is your height in meters? "))
weight = float(input("What is your weight in kg? "))

# Calculate the square of height
height_squared = height ** 2

# Calculate BMI
bmi = weight / height_squared

# Print the result
print(f"Your BMI is: {bmi}")
