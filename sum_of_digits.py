#!/use/bin/python3
"""Methods determining the sum of digits of an integer number.

@params n    (int) : integer number
@return nsum (int) : sum of digits
"""

def sum_of_digits_m0(n):
    """Method 0."""
    nsum = 0
    if n:
        nsum += (n % 10) + sum_of_digits_m0(n // 10)
    return nsum

def sum_of_digits_m1(n):
    """Method 1."""
    nsum = (n % 10) + sum_of_digits_m1(n // 10) if n else 0
    return nsum

def sum_of_digits_m2(n):
    """Method 2."""
    return (n % 10) + sum_of_digits_m2(n // 10) if n else 0

def sum_of_digits_m3(n):
    """Method 3."""
    nsum = 0
    if n == 0:
        return 0
    else:
        nsum = (n % 10) + sum_of_digits_m3(n // 10)
    return nsum

def sum_of_digits_m4(n):
    """Method 4."""
    if n == 0:
        return 0
    else:
        return (n % 10) + sum_of_digits_m4(n // 10)

def sum_of_digits_m5(n):
    """Method 5."""
    return 0 if n == 0 else (n % 10) + sum_of_digits_m5(n // 10)

def sum_of_digits_m6(n): 
    """Method 6.""" 
    nsum = 0
    while n:     
        nsum += (n % 10)
        n = (n // 10)    
    return nsum

def sum_of_digits_m7(n):
    """Method 7."""   
    nsum = 0
    for digit in str(n): 
        nsum += int(digit)      
    return nsum

def sum_of_digits_m8(n):
    """Method 8."""
    digits = []
    nstr = str(n)
    for x in nstr:
        digits.append(int(x))
    nsum = sum(digits)
    return nsum

def sum_of_digits_m9(n):
    """Method 9."""
    nstr = str(n)
    digits = [int(x) for x in nstr]
    nsum = sum(digits)
    return nsum

def sum_of_digits_m10(n):
    """Method 10."""
    nsum = sum(int(digit) for digit in str(number))
    return nsum

def sum_of_digits_m11(n):
    """Method 11."""
    snum = str(n)
    nsum = sum(int(s) * snum.count(s) for s in "123456789")
    return nsum

def sum_of_digits_m12(n):
    """Method 12."""
    nsum = sum(map(int, str(n)))
    return nsum

def sum_of_digits_m13(n):
    """Method 13."""
    nstr = str(n)
    nsum = 0
    for i in range(0, len(nstr)):
        nsum += int(nstr[i])
    return nsum

def sum_of_digits_m14(n):
    """Method 14."""
    nsum = 0
    while n:
        nsum, n = nsum + (n % 10), (n // 10)
    return nsum

def sum_of_digits_m15(n):
    """Method 15."""
    nsum = 0
    while n:
        n, rest = divmod(n, 10)
        nsum += rest
    return nsum

def sum_of_digits_m16(n):
    """Method 16."""
    nsum = 0
    while n: 
        take = divmod(n, 10) 
        nsum += take[1]
        n = take[0] 
    return nsum

def sum_of_digits_m17(n):
    """Method 17."""
    nsum = 0
    for i in range(len(str(n))):
        nsum += ord(str(n)[i]) - 48
    return nsum




