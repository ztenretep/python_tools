#!/use/bin/python3
"""Calculate the Harshad numbers."""

# Function checksum
def checksum(n):
    cs = 0
    while n > 0:
        cs += int(n % 10)
        n = n // 10
    return cs

# Print result to screen.
for i in range (1, 101):
    if int(i * 10.0 / checksum(i)) % 10 == 0:
        print(i)
