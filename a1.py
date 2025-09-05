# Assignment 1: AI-Generated Python Problems
# Name: [Alexander Schildgen]

"""
AI-Generated Problem Set

INSTRUCTIONS:
1. Document your original AI prompt below
2. Copy the problems your AI assistant generated
3. Implement solutions for each problem
4. Include comments explaining your approach
5. Test your solutions with different inputs

Remember: The goal is to LEARN, not just get working code!
"""

# =============================================================================
# PART 1: DOCUMENT YOUR AI COLLABORATION
# =============================================================================

"""
MY ORIGINAL AI PROMPT:
I'm learning Python basics in a high school programming class. I have some experience 
with Java. Can you create 5-7 practice problems that cover: > - Variables
 and basic data types > - Conditionals (if/elif/else) > - Loops (for and
 while) > - Functions > - Basic list operations > > Make them
 progressively more challenging. Make sure each problem has clear
 instructions and example inputs/outputs.

Example: "I'm learning Python basics in a high school programming class. 
I have some experience with Java. Can you create 5-7 practice problems that cover..."
"""

# =============================================================================
# PART 2: AI-GENERATED PROBLEMS & SOLUTIONS
# =============================================================================

"""
# Problem 1: Favorite Number

# Instructions:
# Create a variable called name and assign it your name.
# Create a variable called favorite_number and assign it your favorite number.
# Print the message:
# "Hi, my name is <name> and my favorite number is <favorite_number>."

# Example Output:
# Hi, my name is Taylor and my favorite number is 42.
"""
name = "Alex"
favoriteNumber = 24
print("Hello My name is " + name + " and my favorite number is " + str(favoriteNumber) + ".")

"""
# Problem 2: Temperature Check

# Instructions:
# Ask the user to enter the temperature (in °F).
# Then, print a message based on the temperature:
# - Below 50: "It's cold!"
# - 50 to 80: "Nice weather."
# - Above 80: "It's hot!"

# Example Input/Output:
# Enter the temperature: 72
# Nice weather.
"""
temperature = input("Enter the temperature in F: ")
if int(temperature)<50:
    print("It's cold!")

if int(temperature)>50 & temperature<80:
    print("Nice weather.")

if int(temperature)>80:
    print("It's Hot")

"""
PROBLEM 1: [Problem Title/Description]
[Copy the complete problem description from your AI assistant]

Example:
Problem: Write a function called 'is_even' that takes an integer and returns 
True if the number is even, False if it's odd.

Example inputs/outputs:
- is_even(4) should return True
- is_even(7) should return False



PROBLEM 1: [Problem Title/Description]
[Copy the complete problem description from your AI assistant]

Example:
Problem: Write a function called 'is_even' that takes an integer and returns 
True if the number is even, False if it's odd.

Example inputs/outputs:
- is_even(4) should return True
- is_even(7) should return False



PROBLEM 1: [Problem Title/Description]
[Copy the complete problem description from your AI assistant]

Example:
Problem: Write a function called 'is_even' that takes an integer and returns 
True if the number is even, False if it's odd.

Example inputs/outputs:
- is_even(4) should return True
- is_even(7) should return False
"""












# =============================================================================
# PART 3: TESTING YOUR SOLUTIONS
# =============================================================================


"""
Test all your solutions with different inputs

Add asserts if you feel comfortable

Example:
print("Testing Problem 1:")
print(f"is_even(4): {is_even(4)}")  # Should print True
print(f"is_even(7): {is_even(7)}")  # Should print False
"""

print("Testing Problem 1:")
# Add your tests here

print("\nTesting Problem 2:")
# Add your tests here

print("\nTesting Problem 3:")
# Add your tests here

print("\nTesting Problem 4:")
# Add your tests here

print("\nTesting Problem 5:")
# Add your tests here


