#!/usr/bin/python3
"""Calculate Pi using Chudnovsky formula.

First try of implementing an algorithm based on a(n) / a(n-1).

Results have to be checked carefully.
"""
# pylint: disable=invalid-name

# Import Standard Python modules.
import os
import math
from decimal import Decimal, getcontext, Context, setcontext

# Clear screen.
os.system('clear')

# ===================
# Function pi(places)
# ===================
def pi(places):
    """Calculate the digits of Pi using Chudnovsky formula.
    """
    # Set shortcut for Decimal.
    D = Decimal
    # Set theprecision
    getcontext().prec = places + 2
    # Set the constants.
    d0 = D('13591409')
    d1 = D('545140134')
    n1 = D('426880')
    n2 = D('10005')
    x1 = D('640320')
    x0 = D('24')
    x = x1 * x1 * x1 / x0
    # Set the initial values.
    pi_dec = None
    a_k = D('1')
    a_sum = D('1')
    b_sum = D('0')
    c = D('0')
    total = D('0')
    a_prevsum = D('0')
    k = D('0')
    while True:
        k += D('1')
        a_k *= -1 * (6 * k - 5) * (2 * k - 1) * (6 * k - 1)
        print(a_k)
        a_k /= (k * k * k * x)
        a_sum += D(a_k)
        b_sum += D(k) * D(a_k)
        if a_sum == a_prevsum:
            break
        a_prevsum = D(a_sum)
    total = d0 * a_sum + d1 * b_sum
    c = Decimal(n1) * D(n2).sqrt()
    pi_dec = D(c) / D(total)
    pi_str = str(pi_dec)[:places+2]
    return pi_str

# Set number of places.
PLACES = 100

# Print Pi.
print(pi(PLACES))
