from math import *
import time

def Eratosthenes(n):
    prime_list=[]
    for i in range(2,n+1):
        prime_list.append(i)
    n_sqrt=sqrt(n)
    rounded_n=floor(n_sqrt)
    for i in range(2, rounded_n):
        if prime_list[i]!=0:
            j=i*i
            for j in range(i*i, n+1,i):
                if j not in prime_list:
                    j=j+i
                else:
                    prime_list.remove(j)
            j=i*i

print("N\tEratosthenes")
for t in range(100, 10000, 300):
    start = time.clock()
    result = Eratosthenes(t)
    time1 = time.clock() - start

    print(t, "\t", time1)




