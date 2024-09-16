def whatday(num):
    days = ["None","Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]7
# Check if the number is between 1 and 7
    if num < 1 or num > 7:
        return "wrong, please enter a number between 1 and 7"
    else:
        return days[num]
# Get user input and convert it into an integer
user_input=int(input("Enter a number between 1 and 7: "))

# Call function and print result
print(whatday(user_input))