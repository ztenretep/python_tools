#!/usr/bin/python3
"""Calculate Pi using Chudnovsky formula.

First try of implementing an algorithm based on a(n) / a(n-1).
It is unclear if an arbitrary start value can be used like some
people have demonstrated.

I will set up two version the one which runs over all iterations 
and one which should start with an arbitrary start value.

Results have to be checked carefully.
"""
# pylint: disable=invalid-name

# Import Standard Python modules.
import os
import math
from decimal import Decimal, getcontext, Context, setcontext

# Clear screen.
os.system('clear')

# =============
# Function pi()
# =============
def pi(places=100):
    """Calculate the digits of Pi using Chudnovsky formula.
    """
    # Set shortcut for Decimal.
    D = Decimal
    # Create initial value.
    extra = 3
    a0 = D(10) ** (places + extra)  
    # Set theprecision
    setcontext(Context(clamp=1))
    getcontext().prec = places + extra
   
    # Set the constants.
    d0 = 13591409
    d1 = 545140134
    n1 = 426880
    n2 = 10005
    x1 = D('640320')
    x0 = D('24')
    x = x1 * x1 * x1 / x0
    # Set the initial values.
    a_k = a0
    a_sum = a0
    b_sum = 0
    k = 1
    # Run an infinite loop.
    while 1:
        # Sum up the terms.
        a_k *= -(6*k-5)*(2*k-1)*(6*k-1)
        a_k //= k * k * k * x   
        a_sum += a_k
        b_sum += k * a_k
        k += 1
        # Abort criterion.
        if a_k == 0:
            break
    # Calculate the total sum.
    total = d0 * a_sum + d1 * b_sum
    c = Decimal(n1) * D(n2).sqrt() * D(a0)
    pi_dec = D(c) / D(total)
    pi_str = str(pi_dec)[:places+2]
    return pi_str

# Set number of places.
PLACES = 100

# Print Pi.
print(pi(PLACES))
