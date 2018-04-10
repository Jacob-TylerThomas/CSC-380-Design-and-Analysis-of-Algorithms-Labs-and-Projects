import time
from random import *

def Bubblesort(alist):
    for i in range(0, len(alist)-1):
        for j in range(0, (len(alist)-1)-i):
            if alist[j+1]<alist[j]:
                alist[j+1],alist[j]=alist[j],alist[j+1]
    return alist

# bubbleList=[]
# for i in range (0, 15):
#     bubbleList.append(randint(0, 10000))
#
# selectionList=bubbleList

#print(Bubblesort(bubbleList))

def Selectionsort(alist):
    for i in range(0, len(alist)-1):
        min=i
        for j in range (i+1, len(alist)):
            if alist[j]<alist[min]:
                min=j
        if min!=i:
            alist[i],alist[min]=alist[min],alist[i]
    return alist

#print(Selectionsort(bubbleList))

print("N\tBubblesort\tSelectionsort")
for n in range(100, 3000, 150):
    firstList=[]
    for i in range (0, n):
        firstList.append(randint(0, 10000))

    secondList=list(firstList)


    start = time.clock()
    result = Bubblesort(firstList)
    time1 = time.clock() - start

    firstList=[]

    start = time.clock()
    result = Selectionsort(secondList)
    time2 = time.clock() - start

    secondList=[]

    print(n, "\t", time1, "\t", time2)


