"""
A prime number is a natural number that is only divisible by 1 and by itself.

it is enough if we traverse upto the root of a number. Whenever we find a divisor, 
we print it and also print the quotient. If the quotient is same, we ignore it. 
Because, root of a perfect square will give same quotient as itself.
quotients are the numbers that are on the other side of the root.
So, its okay if we stop traversing at root.
"""

import math


def isPrime(n):
    # print(math.floor(math.sqrt(n)))
    for i in range(2,math.floor(math.sqrt(n))+1):
        if n%i==0:
            return "Not Prime Number"
    return "is Prime Number"

print(isPrime(6))