"""
Armstrong Numbers are the numbers having the sum of digits raised to power no. of digits is 
equal to a given number.
"""

def armstong(n):
    pow = len(str(n))
    num = 0
    x =n
    while(x!=0):
        num += (x%10)**pow
        x=x//10
    if n==num:
        return "yes"
    else:
        return "No"

print(armstong(13))