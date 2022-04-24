#!/use/bin/python3
"""Number of decimal places.

Remarks:

Python floating point numbers are internally represented as binary
rather than decimal numbers. Dealing with decimal places needs strings
or converting float to decimal. A string can converted to decimal, but
this will tack on zeros to get the needed accuracy, or it will be
necessary the rounding setting to truncate it. 

Best way seems to be to work with strings to count decimal places.

@params fnum           (str) : String representation of decimal number
@return decimal_places (int) : Number of decimal places
"""

def decimal_places_m0(fnum):
    """Method 0.
   
    If fnum is of type float the determination of the decimal places
    will fail. fnum must be of type Str here.

    Decimal('0.49') != Decimal(0.49)
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
