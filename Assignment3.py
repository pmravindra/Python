# Pradeep Ravindra
# This program requests inputs from a user and prints out a response

# Receive user input of First and Last Name
fname = input("What is your first name?")
lname = input("What is your last name?")

# Receive user input of integer
number = input("Enter a positive integer greater than 10.")

# Convert user input of integer to number, apply modulo, and add 1
augment = (int(number))%9 + 1

# Print First and Last Name
print (fname +" " + lname)

# Print Conversion
print ("This number may figure significantly in your life in the near future:" + repr(augment))
