#  brute force method

def gcd(n1,n2):

    gcd = 1
    for i in range(1,min(n1,n2)+1):
        if n1%i==0 and n2%i==0:
            gcd = i
    return gcd

print(gcd(144,256))


# using eucledian distance

def gcdByEucledian(n1,n2):
    if n2==0:
        return n1
    return gcdByEucledian(n2,n1%n2)

print(gcdByEucledian(144,256))