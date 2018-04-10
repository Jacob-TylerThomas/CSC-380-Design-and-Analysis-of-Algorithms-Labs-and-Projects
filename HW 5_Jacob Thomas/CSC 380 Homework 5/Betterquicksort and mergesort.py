import time
from random import *

def mergeSort(alist):
    if len(alist)>1:
        mid=len(alist)//2
        leftHalf=alist[:mid]
        rightHalf=alist[mid:]

        mergeSort(leftHalf)
        mergeSort(rightHalf)

        merge(leftHalf, rightHalf, alist)

        return alist

def merge(leftHalf, rightHalf, alist):
    i=0
    j=0
    k=0

    while i<len(leftHalf) and j<len(rightHalf):
        if leftHalf[i]<=rightHalf[j]:
            alist[k]=leftHalf[i]
            i+=1
        else:
            alist[k]=rightHalf[j]
            j+=1
        k+=1

    while i<len(leftHalf):
        alist[k]=leftHalf[i]
        i=i+1
        k=k+1

    while j<len(rightHalf):
        alist[k]=rightHalf[j]
        j=j+1
        k=k+1
def quickSort(alist, left, right):

    if left<right:

        s = BetterHoarePartition(alist,left,right)

        quickSort(alist,left,s-1)
        quickSort(alist,s+1,right)

    return alist

def BetterHoarePartition(alist, left, right):
   newPivotValue=newMedian((left+right)//2, left, right, alist)
   alist[left], alist[newPivotValue]=alist[newPivotValue], alist[left]
   p = alist[left]
   i = left + 1
   j = right

   boolean = False
   while not boolean:

       while i <= j and alist[i] <= p:
            i+=1

       while alist[j] >= p and j >= i:
            j-=1

       if j < i:
           boolean = True
       else:
           alist[i], alist[j]=alist[j], alist[i]

   alist[left], alist[j]=alist[j], alist[left]

   return j

def newMedian(pivot, left, right, alist):
    if alist[left]<alist[right]:
        if alist[right]<alist[pivot]:
            return right
        else:
            return pivot

    else:
        if alist[left]<alist[pivot]:
            return left
        else:
            return pivot

myList=[8, 3, 2, 9, 7, 1, 5, 4]
print(mergeSort(myList))
print(quickSort(myList, 0, len(myList)-1) )

print("N\tMergesort\tBetterQuicksort")
for n in range(10000, 1000000, 50000):
    firstList=[]
    for i in range (0, randrange(400, 500)):
        firstList.append(randint(0, 10000))
    firstList.sort()

    secondList=[]
    for i in range (0, randrange(500, 600)):
        secondList.append(randint(0, 10000))
    secondList.sort()

    firstList.append(secondList)

    firstSortedList=[firstList]
    secondSortedList=list(firstSortedList)

    start = time.clock()
    result = mergeSort(secondSortedList[:])
    time1 = time.clock() - start

    firstList=[]
    firstSortedList=[]

    start = time.clock()
    result = quickSort(secondSortedList, 0, len(secondSortedList)-1)
    time2 = time.clock() - start

    secondList=[]
    secondSortedList=[]

    print(n, "\t", time1, "\t", time2)
