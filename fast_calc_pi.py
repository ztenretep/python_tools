#!/usr/bin/env python
"""Fast calculation of Pi."""

# Import the standard Python modules.
import decimal

# Set the constant.
DECIMAL_PLACES = 100

# ==================================
# Function pi_gauss_legendre(places)
# ==================================
def pi_gauss_legendre(places):
    precision = places + 2
    decimal.getcontext().prec = precision
    D = decimal.Decimal
    with decimal.localcontext() as ctx:
        ctx.prec += 2
        two = D('2') 
        four = D('4')   
        a, b, t, p = 1, 1/two.sqrt(), 1/four, 1
        pinew = None
        while 1:
            a1    = (a + b) / two
            b     = (a * b).sqrt()
            t    -= p * (a - a1) * (a - a1)
            a, p  = a1, two * p
            piold = pinew
            pinew = ((a + b) * (a + b)) / (four * t)
            if pinew == piold:
                break
    pi = str(+pinew)[:precision]
    return pi

PI = '3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'
print("Reference:")
print(PI)

print("From Gauss-Legendre:")
pi_calc = pi_gauss_legendre(DECIMAL_PLACES)
print(pi_calc)

if PI != pi_calc:
    print("ERROR in calculation!")
