# Pradeep Ravindra
# This program uses regular expression (regex) operations to extrapolate data from a .txt file and reorder it

import sys
import re

# Looks for UAlbanyLightning.txt using try/catch
try:
    f = open("UAlbanyLightning.txt")
except OSError:
    print("File not found.")
    sys.exit(0)

# Reads .txt file line by line
for line in f:

    # Looks for a specified pattern to extrapolate dates using regex
    date = (re.findall(r'([0-9]{4})-([0-1][0-9])-([0-3][0-9])', line ))

    # Looks for a specified pattern to extrapolate the number of lightning strikes using regex
    strikes = (re.findall(r'([0-9]+)', line ))

    # If the date array has an element, this will print a reordered date followed by the number of lightning strikes
    if (not date) == False:
        print (date[0][1] + " " + date[0][2] + " " + date[0][0] + ": " + strikes[-1] + " lightning strikes were recorded.")
