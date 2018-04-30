# Pradeep Ravindra
# This program receives an IP address as an input and validates it

# Receives user input
ip = input("Please enter an IP address.  A valid format is x.x.x.x where x is an integer that ranges from 0 to 255: ")

# Initializes Counter
i = 0

# Prints user input
print ("You entered: " + ip)

try:
    # Tokenizes user input
    iptoken = ip.split(".")

    # Validates IP address length
    if len(iptoken) != 4:
        print ("Invalid IP Address.  Some numbers are missing!")
    else:
        for i in range (0, len(iptoken)):

            # Stores token in x
            x = int(iptoken[i])

            # Validates section value by checking token
            if x > 255:
                print("Section " + repr(i+1) + " is out of range.  It is greater than 255.")
            elif x < 0:
                print("Section " + repr(i+1) + " is out of range.  It is less than 0.")
            else:
                print("Section " + repr(i+1) + " is correct.")

            # Counter increments
            i = i + 1

# Catches error if user input is not an integer,
except ValueError:
    print("Error!  IP Address input contains letters in section " + repr(i+1) + ".  Please try again.")
