#!/use/bin/python3
"""Calculate the Harshad numbers.
"""

# Function checksum()
def checksum(n):
    cs = 0
    while n > 0:
        cs += int(n % 10)
        n = n // 10
    return cs

# Function is_hashard()
def is_hashard(i):
    if i % checksum(i) == 0:
        return True
    return False

# Print result to screen.
for i in range (1, 101):
    if is_hashard(i) == True:
        print(i)
