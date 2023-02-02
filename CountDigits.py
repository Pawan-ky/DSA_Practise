def countDigits(n):
    x = n
    cnt = 0
    while(x!=0):
        x = x//10
        cnt+=1
    return cnt

print(countDigits(12345))