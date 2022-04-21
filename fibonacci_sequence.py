#!/usr/bin/python3
"""Recursive Fibonacci element calculation.

The Fibonacci numbers are the elements form the Fibonacci sequence, in which
each number is the sum of the two preceding numbers. The function that represents
this is F(n) = F(n-1) + F(n-2). The functional values 0 and 1 are special ones.

The Fibonacci sequence looks like:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, ...
"""
# pylint: disable=useless-return
# pylint: disable=invalid-name
# pylint: disable=unused-argument

# Import the standard Python modules.
import sys
import signal

# -------------------------
# Define the signal handler
# -------------------------
def signal_handler(signum, frame):
    """Define the signal handler."""
    # Print message to screen.
    print('You pressed Ctrl+C!')
    # Exit script.
    sys.exit(0)

# Set constant.
N = 21

# ====================
# Function fibonacci()
# ====================
def fibonacci(n):
    """Fibonacci series element calculation."""
    # Check the special cases 0 and 1.
    if n in {0, 1}:
        # Return the Fibonacci element.
        return n
    # Return the Fibonacci element.
    return fibonacci(n - 1) + fibonacci(n - 2)

# ==========
# Print list
# ==========
def print_list(n):
    """ Print Fibonacci sequence as list."""
    # Print headline to screen.
    print("{0}".format("Fibonacci Sequence:"))
    # Print Fibonacci as list.
    print((str([fibonacci(ele) for ele in range(n)])[1:-1]))
    # Return None
    return None

# ===========
# Print table
# ===========
def print_table(n):
    """ Print Fibonacci sequence as table."""
    # Print headline to screen.
    print("{:<10}{:<}".format("Element", "Fibonacci Number"))
    # Loop over the range of N.
    for ele in range(n):
        # Print value and functional value.
        print("{:<10}{:<}".format(ele, fibonacci(ele)))
        # Print result to screen.
    # Return None
    return None

# ++++++++++++++++++++
# Main script function
# ++++++++++++++++++++
def main(n):
    """Main script function."""
    # Print Fibonacci as table.
    print_table(n)
    # Print Fibonacci as list.
    print_list(n)
    # Return None
    return None

# Execute script as program or as module.
if __name__ == "__main__":
    # register the signal handler.
    signal.signal(signal.SIGINT, signal_handler)
    # Call the main script function.
    main(N)
