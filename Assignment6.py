# Pradeep Ravindra

# This program generates random numbers in the range of 1 to 500 until the number 500 is generated

# Random Number Generator
import random

# Initializing variables
y = 0
x = 0
i = 0

# While loop that runs until the number 500 is generated
while x < 500:

    # Generates a random number within the range of 1 and 500 and stores it as x
    x = random.randint(1,500)

    # Iteration counter
    i = i + 1

    # Conditional test to determine if an iteration has generated the highest number thus far and stores it as y
    if x > y:
        y = x
        print ("The largest integer so far is " + repr(y))

    # Conditional test to print number of iterations if while loop termination condition is met
    if x == 500:
        print ("It took " + repr(i) + " iterations to generate the number 500.")
