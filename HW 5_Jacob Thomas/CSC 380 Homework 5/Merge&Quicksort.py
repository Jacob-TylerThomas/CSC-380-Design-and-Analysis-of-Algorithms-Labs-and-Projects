import time
from random import *
#Disclaimer: The pseudocode could not be implemented fully so I have used some code given to me by Guinn

def mergeSort(alist):
    if len(alist)>1:
        mid=len(alist)//2
        leftHalf=alist[:mid]
        rightHalf=alist[mid:]

        mergeSort(leftHalf)
        mergeSort(rightHalf)

        merge(leftHalf, rightHalf, alist)

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

my_list=[8, 3, 2, 9, 7, 1, 5, 4]

mergeSort(my_list)
print(my_list)

def quickSort(alist, left, right):

    if left<right:

        s = HoarePartition(alist,left,right)

        quickSort(alist,left,s-1)
        quickSort(alist,s+1,right)

    return alist

def HoarePartition(alist, left, right):
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

myList=[5, 3, 1, 9, 8, 2, 4, 7]
print(quickSort(myList, 0, len(myList)-1) )
print("N\tMergesort\tQuicksort")
for n in range(10000, 1000000, 50000):
    firstList=[]
    for i in range (0, n):
        firstList.append(randint(0, 10000))

    secondList=list(firstList)


    start = time.clock()
    result = mergeSort(firstList)
    time1 = time.clock() - start

    firstList=[]

    start = time.clock()
    result = quickSort(secondList, 0, len(secondList)-1)
    time2 = time.clock() - start

    secondList=[]

    print(n, "\t", time1, "\t", time2)


