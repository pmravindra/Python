# Pradeep Ravindra

# Displays a random proverb based on user input

# System Utility
import sys

# Welcome Message
print ("Welcome!  This is a proverb generator.")

# User Input Request
number = input("Please enter a positive integer. ")

# Input Validation
try:
    intx = int(number)
    if intx <= 0:
        print ("Input was a non-positive integer.  Please try again.")
        sys.exit(0)
except ValueError:
    print ("That's not a valid input.")
    sys.exit(0)

# User Input Confirmation Message
print ("You entered the number", repr(intx) + ".")

# Modulo Augmentation to reference Output Statement
convert = intx%7

# Proverb if-elif generator.  Source: http://www.phrasemix.com/collections/the-50-most-important-english-proverbs
# Output Statements
if convert == 0:
    print ("Two wrongs don't make a right.")
    print ("Explanation: When someone has done something bad to you, trying to get revenge will only make things worse.")
elif convert == 1:
    print ("The pen is mightier than the sword.")
    print ("Explanation: Trying to convince people with ideas and words is more effective than trying to force people to do what you want.")
elif convert == 2:
    print ("When in Rome, do as the Romans.")
    print ("Explanation: Act the way that the people around you are acting. This phrase might come in handy when you're traveling abroad notice that people do things differently than you're used to.")
elif convert == 3:
    print ("The squeaky wheel gets the grease.")
    print ("Explanation: You can get better service if you complain about something. If you wait patiently, no one's going to help you.")
elif convert == 4:
    print ("When the going gets tough, the tough get going.")
    print ("Explanation: Strong people don't give up when they come across challenges. They just work harder.")
elif convert == 5:
    print ("No man is an island.")
    print ("Explanation: You can't live completely independently. Everyone needs help from other people.")
elif convert == 6:
    print ("Fortune favors the bold.")
    print ("Explanation: People who bravely go after what they want are more successful than people who try to live safely.")
