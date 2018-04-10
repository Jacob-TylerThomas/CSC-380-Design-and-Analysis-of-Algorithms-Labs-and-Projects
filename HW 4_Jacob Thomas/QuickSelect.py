from LomutoPartition import *
import time
from random import *

def QuickSelect(alist,k):
    left=0
    right=len(alist)
    s=LomutoPartition(alist, left, right)
    if s==k-1:
        print(alist[s])
    elif s>left + k-1:
        return QuickSelect(alist[:s-1],k)
    else:
        return QuickSelect(alist[s+1:],k-1-s,)

myList=[8,12,3,4,9,16,1,7,22,52,13]

QuickSelect(myList,7)

# print("N\tInsertionSort")
# for t in range(10):
#     try:
#         timeList=[8,12,3,4,9,15,1,7,22,54]
#         k=randint(1,10)
#         start = time.clock()
#         result = QuickSelect(timeList,k)
#         time1 = time.clock() - start
#
#         timeList=[]
#
#         print(t, "\t", time1)
#
#     except:
#         None