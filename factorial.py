"""
Factorial of N

n*(n-1)*(n-1)*.....1
"""

def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

print(fact(6))
