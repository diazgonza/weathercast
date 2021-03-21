#!/usr/bin/python

import sys

def rainy_probabilioty(date):
    """Calculates the probability of a rainy day"""

    return 0

num_args = len(sys.argv)

# Setting up the program name
pName = sys.argv[0]
k = sys.argv[0].rfind("/")
if k != -1:
    pName = sys.argv[0][k+1:]

# Usage message
if num_args != 2:
    print("Usage: {} [date] (yyyymmdd format)\n".format(pName))
    exit(-1)

# Dates the user is interested in
dates = sys.argv[1]

# Printing the result
result = rainy_probabilioty(dates)

print("Percent chance of rain: {}".format(result))

exit(0)
