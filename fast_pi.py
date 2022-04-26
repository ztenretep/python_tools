#!/usr/bin/python3
"""Calculate the digits of Pi using Chudnovsky formula.

First result of investigation. Results have to be checked.
"""

# Import Standard Python modules.
import os
import math

# Clear screen.
os.system('clear')

def sqrt(num, prec):
    """Return the square root of num as a fixed point number prec.
    """
    # Set the initial value.
    n_prec = num * prec
    # Make an initial guess.
    float_point_prec = 10 ** 16
    # Calculate the initial floating point number.
    n_float = float((n_prec * float_point_prec) // prec) / float_point_prec
    # Calculate the initial square root.
    sr = (int(float_point_prec * math.sqrt(n_float)) * prec) // float_point_prec
    # Run an infinite loop.
    while 1:
        sr_old = sr
        sr = (sr + n_prec // sr) // 2
        # Abort criterion.
        if sr == sr_old:
            break
    # Return square root.
    return sr * prec

def pi_digits(digits=10**200):
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
    # Calculate the constant value.
    c = n1 * sqrt(n2, digits)
    # Finally calculate Pi.
    pi = c // total
    # Return Pi.
    return pi

# Set number of digits.
PLACES = 100

# Create initial value.
exp = 10 ** (2 * PLACES)

# Print Pi.
print(pi_digits(exp))
