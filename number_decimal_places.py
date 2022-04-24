#!/use/bin/python3
"""Number of decimal places.

Remarks:

Python floating point numbers are internally represented as binary
rather than decimal numbers. Dealing with decimal places needs strings
or converting to decimal. 

@params fnum           (str) : String representation of decimal number
@return decimal_places (int) : Number of decimal places
"""

def decimal_places_m0(fnum):
    """Method 0.
    """
    from decimal import Decimal
    dnum = Decimal(fnum)
    ndp = dnum.as_tuple().exponent
    if ndp <= 0:
        return abs(ndp)
    else:
        return 0

def decimal_places_m1(fnum):   
    """Method 1."""
    if fnum.find('.') != -1:
        return len(fnum.split(".")[1])
    else:
        return 0

def decimal_places_m2(fnum):   
    """Method 2."""
    if '.' in fnum:
        return len(fnum.split(".")[1])
    else:
        return 0

def decimal_places_m3(fnum):
    """Method 3."""
    ndp = fnum[::-1].find('.')
    if ndp > 0:
        return ndp
    else:
        return 0

       
   
