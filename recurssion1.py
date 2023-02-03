"""
Print numbers from 1 to N without the help of loops.
"""

def oneTon(n):
 
    if(n==0):
        return
    oneTon(n-1)
    print(n)

oneTon(3)

"""
Print numbers from N to 1 without the help of loops.
"""

def nToOne(n):
    if n==0:
        return
    print(n)
    nToOne(n-1)

nToOne(4)

"""
Print HELLO n times without the loop.
"""

def hello(n):
    
    if n==0:
        return
    hello(n-1)
    print("Hello")

hello(3)