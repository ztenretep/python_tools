#!/usr/bin/python3
"""Determine the number of decimal places.

The script determines the number of decimal places after the decimal point.

First, the decimal number is converted to a string. The string representation
of the decimal number is divided into two parts. The decimal point acts as a
separator. Then the number of digits of the decimal part is determined.
"""

# Set the decimal number.
DECNUM = 3.141592653

# ======================================
# User defined function decimal_places()
# ======================================
def decimal_places(decnum):
    """Function to get the number of decimal places.

    Determine the number of decimal places after the
    decimal point.

    @params  decnum (float) : Decimal number
    @returns number (int)   : Decimal places  
    """
    # Determine the number of decimal places.
    number = len(str(decnum).split('.')[1])
    # Return the number of decimal places.
    return number

# ---------------------
# Main script function.
# ---------------------
def main(decnum):
    """Main script function."""
    # Call function.
    print(decimal_places(decnum))
    # Return None
    return None

# Run script as program or as module.
if __name__ == "__main__":
    # Call the main function.
    main(DECNUM)
