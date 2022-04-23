#!/use/bin/python3
"""Collection of methods for calculating sum of digits.

@params n    (int) : integer number
@return nsum (int) : sum of digits
"""

def sum_of_digits_m0(n):
    """Method 0."""
    nsum = 0
    if n != 0:
        nsum += (n % 10) + sum_of_digits_m0(n // 10)
    return nsum

def sum_of_digits_m1(n):
    """Method 1."""
    nsum = (n % 10) + sum_of_digits_m1(n // 10) if n != 0 else 0
    return nsum

def sum_of_digits_m2(n):
    """Method 2."""
    return 0 if n == 0 else (n % 10) + sum_of_digits_m2(n // 10)

def sum_of_digits_m3(n): 
    """Method 3.""" 
    nsum = 0
    while n:     
        nsum += (n % 10)
        n = (n // 10)    
    return nsum

def sum_of_digits_m4(n):
    """Method 4."""   
    nsum = 0
    for digit in str(n): 
        nsum += int(digit)      
    return nsum

def sum_of_digits_m5(n):
    """Method 5."""
    digits = []
    nstr = str(n)
    for x in nstr:
        digits.append(int(x))
    nsum = sum(digits)
    return nsum

def sum_of_digits_m6(n):
    """Method 6."""
    nstr = str(n)
    digits = [int(x) for x in nstr]
    nsum = sum(digits)
    return nsum

def sum_of_digits_m7(n):
    """Method 7."""
    nsum = sum(int(digit) for digit in str(number))
    return nsum

def sum_of_digits_m8(n):
    """Method 8."""
    snum = str(n)
    nsum = sum(int(s) * snum.count(s) for s in "123456789")
    return nsum

def sum_of_digits_m9(n):
    """Method 9."""
    nsum = sum(map(int, str(n)))
    return nsum

def sum_of_digits_m10(n):
    """Method 10."""
    nstr = str(n)
    nsum = 0
    for i in range(0, len(nstr)):
        nsum += int(nstr[i])
    return nsum

def sum_of_digits_m11(n):
    """Method 11."""
    nsum = 0
    while n:
        nsum, n = nsum + (n % 10), (n // 10)
    return nsum

def sum_of_digits_m12(n):
    """Method 12."""
    nsum = 0
    while n:
        n, remainder = divmod(n, 10)
        nsum += remainder
    return nsum

def sum_of_digits_m13(n):
    """Method 13."""
    nsum = 0
    while n: 
        take = divmod(n, 10) 
        rest = take[1] 
        nsum += rest 
        n = take[0] 
    return nsum



