import math 
def countdigits1(n):
    x = n
    cnt = 0
    while(x!=0):
        x = x//10
        cnt+=1
    return cnt


def countdigits2(n):
    return len(str(n))

def countdigits3(n):
    return math.floor(math.log10(n)+1)



print(countdigits1(123450))
print(countdigits2(123450))
print(countdigits3(123450))

