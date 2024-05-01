# Day 2 

# Topics: Numbers and Strings 
# String concatenation 
# Floats, Integers, and Booleans

# PEMDAS - Parentheses, Exponents, Multiplication, Division, Addition, Subtraction

# Program name: Tip calculator 

# Tip: We count from 0 in Python

# Print a welcome message to the user
print("Welcome to the tip calculator.\n")

# Ask the user for the total bill
bill = float(input("What was the total bill? $"))

# Ask the user for the percentage tip they want to give
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

# Ask the user for the number of people to split the bill
people = int(input("How many people to split the bill? "))

# Calculate the total bill with tip
total_bill = bill + bill * tip / 100

# Calculate the bill per person
bill_per_person = total_bill / people

# Print the bill per person
print(f"Each person should pay: ${bill_per_person:.2f}")

