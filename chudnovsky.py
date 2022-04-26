#!/usr/bin/python3
"""Calculate the digits of Pi using Chudnovsky formula.

First result of investigation. Results have to be checked.
"""

# Import Standard Python modules.
import os
import math
from decimal import Decimal, getcontext

# Clear screen.
os.system('clear')

# =============
# Function pi()
# =============
def pi(digits=100):
    """Calculate the digits of Pi using Chudnovsky formula.
    """
    # Set the constants.
    d0 = 13591409
    d1 = 545140134
    n1 = 426880
    n2 = 10005
    x1 = 640320
    x0 = 24
    x = x1*x1*x1 // x0
    # Set the initial values.
    a_k = digits
    a_sum = digits
    b_sum = 0
    k = 1
    # Run an infinite loop.
    while 1:
        # Sum up the terms.
        a_k *= -(6*k-5)*(2*k-1)*(6*k-1)
        a_k //= k*k*k*x
        a_sum += a_k
        b_sum += k * a_k
        k += 1
        # Abort criterion.
        if a_k == 0:
            break
    # Calculate the total sum.
    total = d0 * a_sum + d1 * b_sum
    c = Decimal(n1) * Decimal(n2).sqrt() * digits
    pi = c / Decimal(total)
    return str(pi)[:PLACES+2]

# Set number of digits.
PLACES = 1000000

# Set the precision.
getcontext().prec = PLACES + 8

# Create initial value.
exp = 10 ** (PLACES + 4)

# Print Pi.
print(pi(exp))
