wordList=['h','a','p','p','y']
characterList=['h','a','p','y','h','p','p','y','h','a','p','p','y','a','p','p','y']

def BruteForceStringMatch(n,m):
    count=0
    for i in range(0, len(n)-len(m)):
        j=0
        while j<len(m) and m[j]==n[i+j]:
            j=j+1
            count+=1
        if j==len(m):
            return i

    return -1

print(BruteForceStringMatch(characterList, wordList))


