
# Sums up the occurence of each element in a list and returns half the summation of each element
# First line -- length of list
# Second line -- Input array values e.g {2 1 3 1 2}

#Checks the frequency of an element in an array
def matchPair(a):
    b = {}
    pairCount = 0
    for i in range(len(a)):
        if a[i] in b.keys():
            value = b[a[i]]
            b[a[i]] = value + 1
        else:
            value = 0
            b[a[i]] = value + 1

    for v in b.values():
        pairCount = pairCount + int(v/2)
    return pairCount


# Queries user for array values
def arrayInput(n):
    N = input().strip().split(" ")
    N = list(map(int,N))
    while arrayInputCheck(N, n) == 1:
        arrayInput()
    return N


# Checks if array values are within constraint
def arrayInputCheck(N, n):
    for i in range(n):
        if N[i] < 1 and N[i] > 100:
            arrayFlag = 1
            return arrayFlag
        else:
            arrayFlag = 0
    return arrayFlag


# Queries user for array length
def arrayLen():
    n = int(input().strip())
    while arrayLenCheck == 1:
        arrayLen()
    return n


# Checks if array length is within constraints
def arrayLenCheck(n):
    if n < 1 and n > 100:
        arrayFlagLen = 1 
        return arrayFlagLen
    return 0


########################################################################################
########## Main Code Block #############################################################

n = arrayLen()
N = arrayInput(n)
print(matchPair(N))

















# Ignore 
'''
a = [2,1,1,2,3,10000]
b = [101]
#a = [1,2,1,2,3,3,2,1]
# Matching Pairs
#b = [2,2,1,1,3,3,4,3,5,4,4,5,5] 
#print(matchPair(b))
'''      