#!/usr/bin/env python
"""Fast calculation of circle number Tau."""

# Import the standard Python modules.
from decimal import Decimal
from decimal import getcontext
from decimal import localcontext

# Set som constants.
PLACES = 100
ALPHAS = PLACES + 2

# Set the precision.
PRECISION = PLACES + 2
getcontext().prec = PRECISION

# ============================
# Function pi_gauss_legendre()
# ============================
def tau_gauss_legendre():
    D = Decimal
    with localcontext() as ctx:
        ctx.prec += 2
        a, b, t, p = D(1), 1/D(2).sqrt(), 1/D(4), D(1)
        tau = None
        while 1:
            an    = (a + b) / 2
            b     = (a * b).sqrt()
            t    -= p * (a - an) * (a - an)
            a, p  = an, 2*p
            tmp = tau
            tau    = (a + b) * (a + b) / (2 * t)
            if tau == tmp:
                break
    tau = +tau
    return tau

print("From Gauss-Legendre:")
tau_calc = str(tau_gauss_legendre())[:ALPHAS]
print(tau_calc)
