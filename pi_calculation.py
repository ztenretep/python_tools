#!/use/bin/python3

# pi calculation n = 4
# tau calculation n = 8
def function_pi(p=2):
    pi = 0
    n = 4
    d = 1
    i = 1
    tmp = 0
    while True:
        sign = 2 * (i % 2) - 1
        pi += sign * (n / d)
        d += 2 
        exp = 10 ** (p+1)
        if int(pi * exp - tmp * exp) == 0:
            break
        tmp = pi
        i += 1
    return pi

print(function_pi(5))
