#!/usr/bin/env python3
"""High precision calculation of circle number Pi.

The implemented algorithm makes use of the so-called Gauss–Legendre algorithm.
As parameter the needed number of digits after the decimal point can be given.

The current version compares Pi with 100 digits after the decimal point from
literature with the the calculated value.

Usage:
    python3 [script_name] <decimal_places>

Testcase:
    100 decimal places act as test case. If no argument is given 100 is used.
    
By increasing the internal precision there is no round error in the last digit.    
"""
# pylint: disable=unused-argument
# pylint: disable=invalid-name
# pylint: disable=useless-return
# pylint: disable=invalid-unary-operand-type

# Import the standard Python modules.
import sys
import signal
import decimal

# -------------------------
# Define the signal handler
# -------------------------
def signal_handler(signum, frame):
    """Define the signal handler."""
    # Print message to screen.
    print('You pressed Ctrl+C!')
    # Exit script.
    sys.exit(0)

# Set the constant.
DECIMAL_PLACES = 100

# Set constant Pi with 100 digits.
PI = '3.14159265358979323846264338327950288419716939937510' \
       '58209749445923078164062862089986280348253421170679'

# ==================================
# Function pi_gauss_legendre(places)
# ==================================
def pi_gauss_legendre(places=100):
    """Gauss-Legendre algorithm."""
    # Set the precision.
    precision = places + 2
    decimal.getcontext().prec = precision
    # Shortcut the module attribute.
    D = decimal.Decimal
    # The with statement changes the active context temporarily.
    with decimal.localcontext() as ctx:
        # Increase the precision temporarily.
        ctx.prec += 2
        # Substitute 2 and 4.
        two = D('2')
        four = D('4')
        # Set the initial values.
        a, b, t, p = 1, 1/two.sqrt(), 1/four, 1
        pinew = None
        # Run an infinite loop.
        while 1:
            # Calculate the necessary terms.
            a1 = (a + b) / two
            b = (a * b).sqrt()
            t -= p * (a - a1) * (a - a1)
            # Remap values of a and p.
            a, p = a1, two * p
            # Store new pi in old pi variable.
            piold = pinew
            # Calculate Pi.
            pinew = ((a + b) * (a + b)) / (four * t)
            # Leave loop.
            if pinew == piold:
                break
    # +pinew rounds the final result back to the default precision.
    pi = str(+pinew)[:precision]
    # Return pi.
    return pi

# ++++++++++++++++++++
# Main script function
# ++++++++++++++++++++
def main(places):
    """Main script function."""
    # Calculate Pi with requested decimal places.
    pi_calc = pi_gauss_legendre(places)
    # Check if decimal_places is equal 100.
    if places == 100:
        # Print reference to screen.
        print("Circle number Pi from reference:")
        print(PI)
        # Print calculation to screen.
        if PI != pi_calc:
            print("ERROR in calculation!")
    # Print calculation to screen.
    print("Circle number Pi from Gauss-Legendre:")
    print(pi_calc)
    # Return None
    return None

# Run script as program or as module.
if __name__ == "__main__":
    # Register the signal handler.
    signal.signal(signal.SIGINT, signal_handler)
    # Get command line argument.
    arg = sys.argv[1] if len(sys.argv) > 1 else None
    # Set the decimal number.
    decimal_places = int(arg) if arg is not None else DECIMAL_PLACES
    # Call the main function.
    main(decimal_places)
