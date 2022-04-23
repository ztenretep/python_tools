#!/use/bin/python3
"""Collection of methods for calculating sum of digits.
"""

def sum_of_digits_m0(n):
    """Method 0."""
    return 0 if n == 0 else (n % 10) + sum_of_digits_m0(n // 10)

def sum_of_digits_m1(n):
    """Method 1."""
    sum = 0
    if n != 0:
        sum += (n % 10) + sum_of_digits_m0(n // 10)
    return sum

def sum_of_digits_m2(n): 
    """Method 2.""" 
    sum = 0
    while (n != 0):     
        sum += (n % 10)
        n = (n // 10)    
    return sum

def sum_of_digits_m3(n):
    """Method 3."""   
    sum = 0
    for digit in str(n): 
        sum += int(digit)      
    return sum

def sum_of_digits_m4(n):
    """Method 4."""
    digits = []
    nstr = str(n)
    for x in nstr:
        digits.append(int(x))
    return sum(digits)

def sum_of_digits_m5(n):
    """Method 5."""
    nstr = str(n)
    digits = [int(x) for x in nstr]
    return sum(digits)


   



