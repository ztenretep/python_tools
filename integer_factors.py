#!/usr/bin/python3
"""Determine the factors of an integer number.
"""

# Declare a list.
divlst = []

# Get user input.
intnum = int(input("Provide an integer number: "))

# Initialise counter.
i = intnum

while i > 0:
    if intnum % i == 0:
        fac = intnum // i        
        divlst.append(fac)
    i -= 1

# Print result to screen.
print(divlst)
