from math import *
import time
from random import *

def BetterBruteForceClosestPair(alist):
    d=inf
    for i in range(0, len(alist)-1):
        for j in range(i+1, len(alist)):
            d=min(d,(alist[i][0] - alist[j][0])**2 + (alist[i][1] - alist[j][1])**2)

    return sqrt(d)

def efficientClosestPairs(p, q):

    if len(p) <=3:
        return BetterBruteForceClosestPair(p)
    else:
        pL=[]
        qL=[]
        pR=[]
        qR=[]
        s=[]
        mid=len(p)//2
        pL.extend(p[:mid])
        qL.extend(q[:mid])
        pR.extend(p[mid:])
        qR.extend(q[mid:])
        dL=efficientClosestPairs(pL, qL)
        dR=efficientClosestPairs(pR, qR)
        d=min(dL, dR)
        m=p[mid-1][0]
        for i in range(len(p)):
            x=p[i][0]
            diff=abs(x-m)
            if diff<d:
                s.append(p[i])
            i+=1

        dminsq=d**2
        num=len(s)
        k=0
        for i in range(num-2):
            k= i + 1
            while k<=num-1 and (s[k][1]-s[i][1])**2<dminsq:
                dminsq=min((s[k][0]-s[i][0])**2 + (s[k][1]-s[i][1])**2, dminsq)
                k+=1
        return sqrt(dminsq)
p=((0, 1), (2, 1), (1, 2), (1, 3))
p=sorted(p, key=lambda x: x[0])
q=sorted(p, key=lambda x: x[1])

print(efficientClosestPairs(p, q))
print(BetterBruteForceClosestPair(p))

print("N\tMergesort\tQuicksort")
for n in range(100, 5000, 250):
    firstList = [( randint(1000000000000, 15000000000000), randint(1000000000000, 15000000000000)) for k in range(n)]
    firstListXSorted=sorted(firstList, key=lambda x: x[0])
    firstListYSorted=sorted(firstList, key=lambda x: x[0])

    start = time.clock()
    result = BetterBruteForceClosestPair(firstList)
    time1 = time.clock() - start

    firstList=[]

    start = time.clock()
    result = efficientClosestPairs(firstListXSorted,firstListYSorted)
    time2 = time.clock() - start

    firstListXSorted=[]
    firstListYSorted=[]

    print(n, "\t", time1, "\t", time2)