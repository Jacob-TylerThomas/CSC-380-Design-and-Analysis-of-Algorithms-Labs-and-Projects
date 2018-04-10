import time
from random import *
def InsertionSort(alist):
    count=0
    for i in range(1, len(alist)):
        v=alist[i]
        j=i-1
        while j>=0 and alist[j]>v:
            alist[j+1]=alist[j]
            j=j-1
            count+=1

        alist[j+1]=v
    return (alist, ("comparison count is: ",count))
    #return (count)
alist=[2,3,10,9,8]

print(InsertionSort(alist))

print("N\tInsertionSort")
# for t in range(100, 3000, 25):
#     timeList=[]
#     for i in range (t):
#         timeList.append(randint(100,10000))
#     start = time.clock()
#     result = InsertionSort(timeList)
#     time1 = time.clock() - start
#
#     timeList=[]
#
#     print(t, "\t", result,)