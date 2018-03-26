# Pradeep Ravindra
# Exam 1
# This program receives two inputs from a user, validates them as positive integers, and then performs an output of the larger and smaller number as well as modular division

# System Utility
import sys

# Asks user for two positive integer inputs
numberOne = input("Please enter a positive integer. ")

# Validates first user input as a positive integer
try:
    intx = int(numberOne)
    if intx < 0:
        print ("Input was a non-positive integer.  Please try again.")
        sys.exit(0)
except ValueError:
    print ("That's not a valid input.")
    sys.exit(0)

numberTwo = input("Please enter another positive integer. ")

# Validates second user input as a positive integer
try:
    inty = int(numberTwo)
    if inty < 0:
        print ("Input was a non-positive integer.  Please try again.")
        sys.exit(0)
except ValueError:
    print ("That's not a valid input!")
    sys.exit(0)

# Modular Division Variables
modone = intx%inty
modtwo = inty%intx

# Determines the larger number/smaller number and carries out modular division.
if intx > inty:
    print ("The larger number is " + repr(intx) + " and the smaller number is " + repr(inty) + ".")
    print ("The result of modular division is " + repr(modone) + ".")
elif inty > intx:
    print ("The larger number is " + repr(inty) + " and the smaller number is " + repr(intx) + ".")
    print ("The result of modular division is " + repr(modtwo) + ".")
else:
    print ("Both numbers are equal: "+ repr(intx) + ".")
