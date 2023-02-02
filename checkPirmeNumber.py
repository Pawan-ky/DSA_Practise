"""
A prime number is a natural number that is only divisible by 1 and by itself.

"""

import math


def isPrime(n):
    # print(math.floor(math.sqrt(n)))
    for i in range(2,math.floor(math.sqrt(n))+1):
        if n%i==0:
            return "Not Prime Number"
    return "is Prime Number"

print(isPrime(6))