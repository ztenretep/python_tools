#!/usr/bin/env python
"""Fast calculation of Pi."""

# Import the standard Python modules.
from decimal import Decimal
from decimal import getcontext
from decimal import localcontext

# Set the constants.
PLACES = 100
ALPHAS = PLACES + 2

# Set the precision.
PRECISION = PLACES + 2
getcontext().prec = PRECISION

# ============================
# Function pi_gauss_legendre()
# ============================
def pi_gauss_legendre():
    D = Decimal
    with localcontext() as ctx:
        ctx.prec += 2
        a, b, t, p = D(1), 1/D(2).sqrt(), 1/D(4), D(1)
        pi = None
        while 1:
            an    = (a + b) / 2
            b     = (a * b).sqrt()
            t    -= p * (a - an) * (a - an)
            a, p  = an, 2*p
            tmp   = pi
            pi    = (a + b) * (a + b) / (4 * t)
            if pi == tmp:
                break
    pi = +pi
    return pi

PI = '3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'
print("Reference:")
print(PI)

print("From Gauss-Legendre:")
pi_calc = str(pi_gauss_legendre())[:ALPHAS]
print(pi_calc)

if PI != pi_calc:
    print("ERROR in calculation!")
