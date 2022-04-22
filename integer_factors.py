#!/usr/bin/python3
"""Determine the factors of an integer number.
"""

# Declare a list.
divlst = []

# Get user input.
intnum = int(input("Provide an integer number: "))

# Initialise counter.
i=1

while i <= intnum:
    if intnum % i == 0:
        factor = intnum // i        
        divlst.append(factor)
    i=i+1
    #else:
    #    i=i+1

# Get list in reverse order.
divlst.reverse()

# Print result to screen.
print(divlst)
