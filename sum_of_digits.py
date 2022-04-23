#!/use/bin/python3
"""Collection of methods for calculating sum of digits.
"""

def sum_of_digits_m0(n):
    """Method 0."""
    return 0 if n == 0 else (n % 10) + sum_of_digits_m0(n // 10)

def sum_of_digits_m1(n):
    """Method 1."""
    nsum = 0
    if n != 0:
        nsum += (n % 10) + sum_of_digits_m0(n // 10)
    return nsum

def sum_of_digits_m2(n): 
    """Method 2.""" 
    nsum = 0
    while (n != 0):     
        nsum += (n % 10)
        n = (n // 10)    
    return nsum

def sum_of_digits_m3(n):
    """Method 3."""   
    nsum = 0
    for digit in str(n): 
        nsum += int(digit)      
    return nsum

def sum_of_digits_m4(n):
    """Method 4."""
    digits = []
    nstr = str(n)
    for x in nstr:
        digits.append(int(x))
    nsum = sum(digits)
    return nsum

def sum_of_digits_m5(n):
    """Method 5."""
    nstr = str(n)
    digits = [int(x) for x in nstr]
    nsum = sum(digits)
    return nsum

def sum_of_digits_m6(n):
    """Method 6."""
    nsum = sum(int(digit) for digit in str(number))
    return nsum

def sum_of_digits_m7(n):
    """Method 7."""
    d = str(n)
    nsum = sum(int(s) * d.count(s) for s in "123456789")
    return nsum





   



