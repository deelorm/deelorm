
#Task -- Move integer in array towards end of array based on d i.e. [1,2,3,4,5] --> [2,3,4,5,1] when d=1
#It moves first array element depending on d, the rotation value
#First input line -- Integer value of array size & the number of rotations to be performed; space separated {5 6} 
#Second input line -- Values of array elements; space separated e.g {3 4 5 6 7}


#Moves first array element to the last index
def rotLInteger(array1):
    temp = array1[0]
    del array1[0]
    array1.append(temp)
    return array1


#Takes user input array and calls rotLInteger function  depending on d
def iterRotInteger(array1, d):
    array2 = []
    for i in range(d):
        array2 = rotLInteger(array1)

#    array2 = list(map(str,array2))
#    array2 = " ".join(array2)
#    return array2
    for i in range(len(array2)):
        print(array2[i], end=" ")
    print("")


#Queries user for list length & number of integer rotations 'd'
def inputParam():
    opParam = input().strip().split(" ")
    opParam = list(map(int,opParam))
    arrayLen = opParam[0]
    opRep = opParam[1]
    return arrayLen, opRep


#Queries user for list/array element values
def inputList():
#    arrayLen, opRep = inputParam()
    array1 = input().strip().split(" ")
    array1 = list(map(int,array1))
    return array1


#Calls the inputParam, inputList functions and returns the call values to inputQueryCheck
def inputQueryCon():
    arrayLen, opRep = inputParam()
    array1 = inputList()
    checkBit = inputQueryCheck(arrayLen, opRep, array1)
    while not checkBit:
        print("Enter new set of inputs: ")
        arrayLen, opRep = inputParam()
        array1 = inputList()
        checkBit = inputQueryCheck(arrayLen, opRep, array1)
    return array1, opRep


#Chceks the validity of user input against constraints
def inputQueryCheck(arrayLen, opRep, array1):
    checkBit = 1
    if len(array1) != arrayLen:
        checkBit = 0
    if opRep < 1 or opRep > arrayLen:
        checkBit = 0
    if arrayLen < 1 and arrayLen > pow(10,5):
        checkBit = 0
    if True:
        for i in range(len(array1)):
            if array1[i] < 1 or array1[i] > pow(10,6):
                checkbit = 0
                break
    if checkBit:
        return 1
    else:
        return checkBit


#######################################################################################################################
########## Main Block of Code #########################################################################################

a,d = inputQueryCon()
iterRotInteger(a, d)


#Extra Test Cases

#a = [2,3,4,5,6]
#d = 2
# 1 <= n <= 10^5
# 1 <= d <= n
# 1 <= a[i] <= 10^6
