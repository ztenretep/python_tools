#!/usr/bin/python3
"""Calculate Pi using modified Chudnovsky formula.

References:
https://docs.python.org/3.8/library/decimal.html
http://www.numberworld.org/digits/Pi/
"""
# pylint: disable=invalid-name

# Import Standard Python modules.
import os
from decimal import Decimal, getcontext, Context, setcontext

# Clear screen.
os.system('clear')

# ===================
# Function pi(places)
# ===================
def pi(places):
    """Calculate Pi using modified Chudnovsky formula.
    """
    # Set shortcut for Decimal.
    D = Decimal
    # Set the precision
    extra = 2
    getcontext().prec = places + extra
    # Initialise the variables.
    c = None
    total = None
    pi_dec = None
    # Set the constants.
    d0 = D('13591409')
    d1 = D('545140134')
    n1 = D('426880')
    n2 = D('10005')
    #x1 = D('640320')
    #x0 = D('24')
    #x = D(x1) * D(x1) * D(x1) / D(x0)
    x = D('10939058860032000')
    # Set the initial values.   
    a_k = D('1')
    a_sum = D('1')
    b_sum = D('0')
    a_prevsum = D('0')    
    k = 0 # Run index is of type int.
    while True:
        k += 1
        a_k *= -1 * (6 * k - 5) * (2 * k - 1) * (6 * k - 1)
        a_k /= k * k * k * x
        a_sum += a_k
        b_sum += k * a_k
        if a_sum == a_prevsum:
            break
        a_prevsum = a_sum
    total = D(d0) * D(a_sum) + D(d1) * D(b_sum)
    c = Decimal(n1) * D(n2).sqrt()
    pi_dec = D(c) / D(total)
    pi_str = str(pi_dec)[:places+2]
    return pi_str

# Set number of places.
PLACES = 100

# Print Pi.
print(pi(PLACES))
