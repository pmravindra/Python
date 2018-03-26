# Pradeep Ravindra
# The purpose of this program is to simulate a magic eight ball
# Receives an input and generate

# Import Random Integer Generator
import random

# Import delay timer
import time

# Ask user for input
question = input("Please enter a yes or no question. ")

# Ask user to press a key to run program
wait = input("Press Enter to continue...")

# Program delay to simulate eight ball
time.sleep(5)

# Generate random integer between 1 and 10
for x in range (1):
    x = random.randint(1,10)

# if elif decision structure to determine output
if x == 1:
    print ("Of course.")
elif x == 2:
    print ("Most definitely.")
elif x == 3:
    print ("The stars themselves say it will be so.")
elif x == 4:
    print ("This has a 100 percent chance of happening.")
elif x == 5:
    print ("Rather cloudy, not sure.")
elif x == 6:
    print ("Impossible to know.")
elif x == 7:
    print ("Such a question is beyond my knowledge.")
elif x == 8:
    print ("I'm afraid the answer is no.")
elif x == 9:
    print ("Definitely not.")
elif x == 10:
    print ("This has a 0 percent chance of happening.")
else:
    print ("Random number generator failure.")
