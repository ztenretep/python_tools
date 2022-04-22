#!/use/bin/python3
"""Calculate a Harshad number sequence.

A Harshad number is an integer number that is divisible by the sum of its
digits.

Start and stop can be given by command line arguments. Otherwise default
values are used.

The Harshad number sequence looks like:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 18, 20, 21, 24, 27, 30, 36, 40, 42, ...
"""
# pylint: disable=invalid-name
# pylint: disable=useless-return
# pylint: disable=unused-argument

# Import the standard Python modules.
import sys
import signal

# Set the constants.
START = 1
STOP = 101

# -------------------------
# Define the signal handler
# -------------------------
def signal_handler(signum, frame):
    """Define the signal handler."""
    # Print message to screen.
    print('You pressed Ctrl+C!')
    # Exit script.
    sys.exit(0)

# ====================
# Function check_sum()
# ====================
def check_sum(n):
    """Function check_sum(n)."""
    # Initialise the check sum variable.
    cs = 0
    # Loop over the digits of the number.
    while n > 0:
        # Add the value of the digit to the check sum.
        cs += int(n % 10)
        # Decrease the number of digits by one.
        n = n // 10
    # Return the check sum.
    return cs

# =====================
# Function is_harshad()
# =====================
def is_harshad(i):
    """Function is_harshad(i)."""
    # Check if it is a Harshad number.
    if i % check_sum(i) == 0:
        # Return is Harshad.
        return True
    # Return is not Harshad.
    return False

# ++++++++++++++++++++
# Main script function
# ++++++++++++++++++++
def main(a, b):
    """Main script function."""
    # Print list to screen.
    print((str(list(filter(
        None, [e if is_harshad(e) else None for e in range(a, b)]
        )))[1:-1]))
    # Return None
    return None

# Execute script as program or as module.
if __name__ == "__main__":
    # Get command line arguments.
    start, stop = sys.argv[1:] if len(sys.argv) > 1 else (None, None)
    # Set start and stop.
    start = int(start) if start is not None else START
    stop = int(stop) if stop is not None else STOP
    # Register the signal handler.
    signal.signal(signal.SIGINT, signal_handler)
    # Call the main script function.
    main(start, stop)
