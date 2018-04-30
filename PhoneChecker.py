# Pradeep Ravindra
# This program receives and validates four separate non-negative integer inputs step-by-step to compute an average

print ("Hello!  Let's check the average number of times you check your phone per hour.")
print ("Please enter the number of times you have checked your phone per hour in the past 4 hours: ")
print ("How many times have you checked your phone in the...")

# Set while condition
x = 1

# Input for hour one
while x == 1:
    h1 = input("First hour?")

    # Validate input as integer
    try:
        int1 = int(h1)
    except ValueError:
        print ("That's not a valid input.")
        continue

    # Validate input as non-negative integer
    if int1 < 0:
        print ("Input cannot be negative.  Please try again.")
        continue
    break

# Input for hour two
while x == 1:
    h2 = input("Second hour?")

    # Validate input as integer
    try:
        int2 = int(h2)
    except ValueError:
        print ("That's not a valid input.")
        continue

    # Validate input as non-negative integer
    if int2 < 0:
        print ("Input cannot be negative.  Please try again.")
        continue
    break

# Input for hour three
while x == 1:
    h3 = input("Third hour?")

    # Validate input as integer
    try:
        int3 = int(h3)
    except ValueError:
        print ("That's not a valid input.")
        continue

    # Validate input as non-negative integer
    if int3 < 0:
        print ("Input cannot be negative.  Please try again.")
        continue
    break

# Input for hour four
while x == 1:
    h4 = input("Fourth hour?")

    # Validate input as integer
    try:
        int4 = int(h4)
    except ValueError:
        print ("That's not a valid input.")
        continue

    # Validate input as non-negative integer
    if int4 < 0:
        print ("Input cannot be negative.  Please try again.")
        continue
    break

# Store values as array
a = [int1, int2, int3, int4]

# Prints mean of array
print(sum(a) / len(a))
