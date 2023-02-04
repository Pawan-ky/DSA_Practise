"""
Count frequency of each element in the array
"""

def countfreq(arr):
    dic = {}
    for ele in arr:
        if ele in dic.keys():
            dic[ele]+=1
        else:
            dic[ele] = 1
    return dic

print(countfreq([1,1,1,2,2,3,4,5,6,6,6,66,6,7,7,7,77]))


"""
Find the highest/lowest frequency element
"""

def highLowFreq(arr):
    dic = {}
    lowest,highest = arr[0],arr[0]
    for ele in arr:
        if ele in dic.keys():
            dic[ele]+=1
        else:
            dic[ele] = 1
        if dic[ele]>dic[highest]:
            highest = ele
        if dic[ele]<dic[lowest]:
            lowest = ele       
    return lowest,highest

print(highLowFreq([1,1,1,2,2,3,4,5,6,6,6,66,6,7,7,7,77,77,77,77,77,77]))