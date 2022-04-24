#!/use/bin/python3
"""Factorial"""

Def factorial(n):
    import math
    fact = math.factorial(n)
    return fact

# Iterative approach

def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact

# Recursive approach

def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n - 1)

def factorial(n): 
    return 1 if (n==1 or n==0) else n * factorial(n - 1)

# While loop approach

def factorial(n):
    fact = 1
    while True:
        if n == 1:
            return fact
        n, fact = n - 1, fact * n

def factorial(n):
    fact = 1
    count = 1
    while count <= n:
        count, fact = count + 1, fact * count
    return fact

# For loop approach

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

# Using map approach

def factorial(n):
    return eval(' * '.join(map(str, range(1, n + 1))))

# Lambda function

factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)

