from random import *
import time

def RussianPeasent(n,m):
    sum=0
    mult=0
    add=0
    div=0
    while n>0:
        if n%2==1:
            sum+=m
            add+=1
        m=2*m
        mult+=1
        n=n//2
        div+=1
        totalOperations=mult+div+add
    return(sum,add, mult, div)
    #return (totalOperations)
#print(RussianPeasent(33, 33))

# print("N\tInsertionSort")
# for t in range(1000000, 1000000000, 100000):
#     n=randint(100000, t)
#     m=randint(100000, t)
#     start = time.clock()
#     result = RussianPeasent(n, m)
#     time1 = time.clock() - start
#
#     print(t, "\t", result)
