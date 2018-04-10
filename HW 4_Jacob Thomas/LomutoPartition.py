def LomutoPartition(alist, left, right):
    p=alist[left]
    s=left
    comparisons=0
    for i in range (left+1, right):
        if alist[i]<=p:
            s=s+1
            comparisons+=1
            alist[s], alist[i]=alist[i], alist[s]
    alist[left], alist[s]=alist[s], alist[left]
    return s
