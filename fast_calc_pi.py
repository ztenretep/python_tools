#!/usr/bin/env python
"""Fast calculation of Pi."""

# Import the standard Python modules.
import decimal

# Set the constant.
PLACES = 100

# ==================================
# Function pi_gauss_legendre(places)
# ==================================
def pi_gauss_legendre(places):
    precision = places + 2
    decimal.getcontext().prec = precision
    D = decimal.Decimal
    with decimal.localcontext() as ctx:
        ctx.prec += 2
        a, b, t, p = 1, 1/D(2).sqrt(), 1/D(4), 1
        pinew = None
        while 1:
            a1    = (a + b) / 2
            b     = (a * b).sqrt()
            t    -= p * (a - a1) * (a - a1)
            a, p  = a1, 2*p
            piold = pinew
            pinew = (a + b) * (a + b) / (4 * t)
            if pinew == piold:
                break
    pi = str(+pinew)[:precision]
    return pi

PI = '3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'
print("Reference:")
print(PI)

print("From Gauss-Legendre:")
pi_calc = pi_gauss_legendre(PLACES)
print(pi_calc)

if PI != pi_calc:
    print("ERROR in calculation!")
