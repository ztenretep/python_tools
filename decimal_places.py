#!/usr/bin/python3
"""Determine the number of decimal places.

The script determines the number of decimal places after the decimal point.

The decimal number is divided into two parts. The decimal point acts as a
separator.Then the number of digits of the decimal part is determined.

"""

# Set the decimal number.
DECNUM = 3.141592653

# Get the number of decimal places after the decimal point.
numbers = len(str(DECNUM.split('.')[1])
