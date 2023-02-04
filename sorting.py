"""
selection sort
"""

def selectionsort(arr):
    for i in range(len(arr)-1):
        mini = i
        for j in range(i,len(arr)):
            if arr[j]<arr[mini]:
                mini = j
        # swapping elements
        temp = arr[i]
        arr[i] = arr[mini]
        arr[mini] = temp    
    return arr

print(selectionsort([2,4,8,5,6,3,1]))


# bubble sort

def bubblesort(arr):
    for i in range(len(arr)-1):
        swaped = 0
        for j in range(i+1,len(arr)):
            if arr[j]<arr[i]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                swaped = 1
        if swaped==0:
            break
    return arr

print(bubblesort([2,4,8,5,6,3,1]))



"""
Insertion Sort
"""

def insertionsort(arr):
    for i in range(len(arr)):
        j = i
        while(j>0 and arr[j-1]>arr[j]):
            temp = arr[j-1]
            arr[j-1] = arr[j]
            arr[j] = temp
            j-=1
    return arr

print(insertionsort([2,4,8,5,6,3,1]))
