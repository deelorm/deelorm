#[2,0,3,4,5]
#Task -- re-order array in ascending order and return minimum number of swaps
#First input --- number of array elements
#Second input --- array elements
#Constraint1 --- 1 <= n<= 10^5
#Constraint2 --- 1 <= arr[i]<= n
def sort(array1):
    temp = 0
    i = 0 
    j = 0
    swapCount = 0

    for i in range(len(array1)-1):
        temp = array1[i]
        swapIndex = -1
        j = i + 1
        while j <= len(array1)-1:
            if temp > array1[j]:
                temp = array1[j]
                swapIndex = j
            j += 1
        if temp < array1[i]:
            del array1[swapIndex]
            array1.insert(i,temp)
            swapCount += 1 
        elif temp == array1[i] and swapIndex != -1:
            del array1[swapIndex]
            array1.insert(i,temp)
            swapCount += 1
            
    return swapCount, array1

def userQuery():
    n = int(input().strip())
    N = input().strip().split(" ")
    N = list(map(int,N))
    checkBit = userQueryCheck(n, N)

    while not checkBit:
        print("Print new set of inputs : ")
        n = int(input().strip())
        N = input().strip().split(" ")
        N = list(map(int,N))
        checkBit = userQueryCheck(n,N)
    return N

def userQueryCheck(n, N):
    checkBit = 1
    if len(N) != n:
        checkBit = 0
    if n < 1 or n > pow(10,5):
        checkBit = 0
    if True:
        for i in range(len(N)):
            if N[i] < 1 or N[i] > n:
                checkBit = 0
    if checkBit:
        return 1
    else:
        return checkBit


#1,2,4,3,6,5,
#1,2,4,3,6,5
#1,2,3,4,6,5
#1,2,3,4,6,5
#a = [2,4,3,6,5,1]
#b = [2,4,3,6,5,1,2]

b = userQuery()
sCount, array1 = sort(b)
print(sCount)
print(array1)