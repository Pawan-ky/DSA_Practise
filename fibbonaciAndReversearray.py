"""
                     reverse an array
"""

from functools import lru_cache


a = [1,2,3,4,5]
# method 1 
print(a[::-1],end='\n')

# method 2
print(list(reversed(a)))

# method 3
#       two pointer mwthod with recursion

def reverse_arr(arr,start_index, end_index):
    if start_index<end_index:
        arr[start_index], arr[end_index] = arr[end_index], arr[start_index]
        reverse_arr(arr, start_index+1, end_index-1)
    return arr

arr = [1,2,3,4,5]
print(reverse_arr(arr,0,4))




"""                        Fibbonaci Series

                        fib(i) = fib(i-1) + fib(i-2)
"""

# Given an integer N. Print the Fibonacci series up to the Nth term.

# method 1

def fib1(n):
    if n==0:
        print(0)
    elif n==1:
        print(0,1)
                    # method 1
    # else:
    #     fib =[0,1]
    #     for i in range(2,n+1):
    #         fib.append(fib[i-1]+fib[i-2])
    #     print(fib)

    #               method 2

    else:
        secondlast = 0
        last =1
        curr =0
        print(secondlast,end=',')
        print(last,end=',')
        for i in range(2, n+1):
            curr = secondlast+last
            secondlast = last
            last = curr
            print(curr,end=',')

# fib1(5)



#  Using Recurrsion

# find nth fibbonci number
@lru_cache             # if lru_cache not used it wil take much much more time for large numbers eg. 50,100
def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)

print(fib(50))