from math import *
from random import *
import time

def BruteForceClosestPair(alist):
    d=inf
    for i in range(1, len(alist)-1):
        for j in range(i+1, len(alist)):
            d=min(d,sqrt((alist[i][0] - alist[j][0])**2 + (alist[i][1] - alist[j][1])**2))
    return d

def BetterBruteForceClosestPair(alist):
    d=inf
    for i in range(1, len(alist)-1):
        for j in range(i+1, len(alist)):
            d=min(d,(alist[i][0] - alist[j][0])**2 + (alist[i][1] - alist[j][1])**2)
    return sqrt(d)

myList = [( randint(0, 100000000000), randint(0, 100000000000)) for k in range(20)]
print(BruteForceClosestPair(myList))
print(BetterBruteForceClosestPair(myList))

print("N\tBFCP\tBBFCP")
for n in range(100, 3000, 150):
    firstList = [( randint(1000000000000, 15000000000000), randint(1000000000000, 15000000000000)) for k in range(n)]



    start = time.clock()
    result = BruteForceClosestPair(firstList)
    time1 = time.clock() - start


    start = time.clock()
    result = BetterBruteForceClosestPair(firstList)
    time2 = time.clock() - start

    print(n, "\t", time1, "\t", time2)