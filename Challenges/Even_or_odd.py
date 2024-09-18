#Function to check whether a number is even or odd
def even_or_odd(number):
    if (number%2)==0:
        return "Even"
    else:
        return"Odd"
# Take user input and convert it into an integer    
number = int(input("Enter a Number: "))

# Call the function and print the result
result =  even_or_odd(number)
print(result)
