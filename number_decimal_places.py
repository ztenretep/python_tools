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
    dexponent = dnum.as_tuple().exponent
    if dexponent <= 0:
        decimal_places = abs(dexponent)
    else:
        return 0
    return decimal_places

def decimal_places_m1(fnum):
    """Method 1."""
    from decimal import Decimal
    dnum = Decimal(fnum)
    dexponent = dnum.as_tuple().exponent
    decimal_places = abs(dexponent) if dexponent <= 0 else 0
    return decimal_places

def decimal_places_m2(fnum):   
    """Method 2."""
    if fnum.find('.') != -1:
        decimal_places = len(fnum.split(".")[1])
    else:
        return 0
    return decimal_places

def decimal_places_m3(fnum):   
    """Method 3."""
    if '.' in fnum:
        decimal_places = len(fnum.split(".")[1])
    else:
        return 0
    return decimal_places

def decimal_places_m4(fnum):   
    """Method 4."""
    decimal_places = len(fnum.split(".")[1]) if '.' in fnum else 0
    return decimal_places

def decimal_places_m5(fnum):
    """Method 5."""
    decimal_places = fnum[::-1].find('.')
    if decimal_places <= 0:
        return O
    return decimal_places

def decimal_places_m6(fnum):
    """Method 6."""
    decimal_places = fnum[::-1].find('.') if fnum[::-1].find('.') > 0 else 0
    return decimal_places

def decimal_places_m7(fnum):
    """Method 7."""
    from decimal import Decimal
    dnum = Decimal(fnum)
    decimal_places = len(str(abs(dnum - int(dnum)))[2:])
    return decimal_places

