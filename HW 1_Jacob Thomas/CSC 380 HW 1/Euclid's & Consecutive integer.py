from math import gcd
import time
from random import *

def euclid(m,n):
    return gcd(m,n)

#p=euclid(5678, 26) //tests to see if the code works
#print("Euclid's answer is:" ,p)

def consecutive(m,n):
    t=min(m,n)
    while t>0:
        if m % t==0 and n % t==0:
            return t
        t-=1

#t=consecutive(5678,26) //tests to see if the code works
#print("Consecutive's answer is:", t)


print("N\tEuclid's\tConsecutive")
for t in range(10000, 10000000, 250000):
    n=randint(10000, 100000000)
    m=randint(10000, 100000000)
    start = time.clock()
    result = euclid(m,n)
    time1 = time.clock() - start

    start = time.clock()
    result = consecutive(m,n)
    time2 = time.clock() - start

    print(n, "\t", time1, "\t", time2)
