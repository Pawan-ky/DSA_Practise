def reverse(n):

    x=n
    num=0
    while(x!=0):
        rem = x%10
        x = x//10

        num = num*10+rem
    return num

print(reverse(123667))
        