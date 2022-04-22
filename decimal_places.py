#!/usr/bin/python3
"""Determine the number of decimal places.

The script determines the number of decimal places after the decimal point.

First, the decimal number is converted to a string. The string representation
of the decimal number is divided into two parts. The decimal point acts as a
separator. Then the number of digits of the decimal part is determined.
"""

# Set the decimal number.
DECNUM = 3.141592653

def decimal_places(decnum):
    # Get the number of decimal places after the decimal point.
    number = len(str(decnum).split('.')[1])
    # Return the number of decimal places.
    return number

def main():
    decimal_places()
    return None
