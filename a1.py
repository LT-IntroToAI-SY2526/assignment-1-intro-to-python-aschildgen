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
def favoriteNumber(name, favoriteNumber):
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
def findTemp(temperature):
    if int(temperature)<50:
        print("It's cold!")
    if int(temperature)>50 & int(temperature)<80:
        print("Nice weather.")
    if int(temperature)>80:
       print("It's Hot")











"""
PROBLEM 3: Print Even Numbers
Topic: Loops (for loop)
Instructions:
Write a program that prints all even numbers from 2 to n 
(inclusive), where n is a positive integer input.

Example inputs/outputs:
-Example:
Input: 10
Output:

2  
4  
6  
8  
10
"""
def findEvens(highest):
    for i in range(0, int(highest)+1, 2):
     print(i)










""""
PROBLEM 4: Factorial Calculator
[Copy the complete problem description from your AI assistant]

Instructions:
Write a function factorial(n) that returns the factorial of a 
non-negative integer n using a while loop. The factorial of 0 is 1.


Example inputs/outputs:
Input: 5
Output: 120
"""
def findFactorial(factorial):
    x = 1
    for i in range(int(factorial), 1, -1):
        x = x*i
    print(x)










"""
PROBLEM 5: List Average
Topic: Basic list operations and functions
Instructions:
Write a function average(numbers) that takes a list of 
numbers and returns their average. If the list is empty, return None.

Example:
Input: [3, 7, 10]
Output: 6.666666666666667.
"""
def findAverage(nums):
    SUM = 0
    for x in nums:
        SUM+=x
    SUM = SUM/len(nums)
    print (SUM)










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
favoriteNumber("Alex", 24)

print("\nTesting Problem 2:")
findTemp(67)

print("\nTesting Problem 3:")
findEvens(10)

print("\nTesting Problem 4:")
findFactorial(5)

print("\nTesting Problem 5:")
findAverage([6,6,6,7,7,7,67])


