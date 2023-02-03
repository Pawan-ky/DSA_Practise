"""Given a number N, find out the sum of the first N natural numbers.
"""

def sumwhile(n):
    s = 0
    while(n!=0):
        s+=n
        n-=1
    print(s)

sumwhile(6)


# by usng formula   n(n+1)/2

def formulasum(n):
    print(n*(n+1)//2)

formulasum(6)