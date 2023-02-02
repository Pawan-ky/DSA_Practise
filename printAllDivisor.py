"""
it is enough if we traverse upto the root of a number. Whenever we find a divisor, 
we print it and also print the quotient. If the quotient is same, we ignore it. 
Because, root of a perfect square will give same quotient as itself.
quotients are the numbers that are on the other side of the root.
So, its okay if we stop traversing at root.

"""


import math




def divisor(n):
    for i in range(1,math.floor(math.sqrt(n))+1):
        if n%i==0:
            print(i)
        if i!=n//i:
            print(n//i)
        
divisor(12)