
#Task -- find the number of elements pair that have a differnce equal to a target value
# First line -- Input length and target difference value e.g. {4 1}
# Second line -- User array e.g. {1 2 3 4}


# Iterates through array and returns number of array pairs with difference matching target values
def diffPair(array1, tval):
    result = {}
    dictkey = 1
    i = 0
    var1 = []
    while i <= len(array1)-2:
        j = i + 1
        while j <= len(array1)-1:
            arr1 = array1[i]
            arr2 = array1[j]
            if arr1 < arr2:
                var3 = arr1
                arr1 = arr2
                arr2 = var3

            varDiff = arr1 - arr2
            var1 = []
            if varDiff == tval:
                var1.append(arr1)
                var1.append(arr2)
                result[dictkey] = var1
                dictkey += 1
            j += 1
        i += 1
    return len(result)


# Query user for list length & difference target value
def inputParam():
    input1 = input().strip().split(" ")
    input1 = list(map(int,input1))
    return input1


# Query user for array/list input
def arrayInput():
    array1 = input().strip().split(" ")
    array1 = list(map(int, array1))
    return array1


# Calls inputParam & arrayInput and returns function calls to inputCheck
def inputCon():
    input1 = inputParam()
    array1 = arrayInput()
    checkBit = inputCheck(input1, array1)
    while not checkBit:
        input1 = inputParam()
        array1 = arrayInput()
        checkBit = inputCheck(input1, array1)
    return array1, input1


# Compares user input against constraints to check validity
def inputCheck(input1, array1):
    checkBit = 1
    if len(array1) != input1[0]:
        checkBit = 0
        return checkBit
    if input1[0] < 2 or input1[0] > pow(10,5):
        checkBit = 0
        return checkBit
    if input1[1] < 0 or input1[1] > pow(10,9):
        checkBit = 0
        return checkBit
    if checkBit:
        for i in range(len(array1)):
            if array1[i] < 0 or array1[i] > pow(2,31)-1:
                checkBit = 0
                return checkBit
    if checkBit:
        for i in range(len(array1)-1):

            for j in range(i+1, len(array1)):
                if array1[i] == array1[j]:
                    checkBit = 0
                    return checkBit
#                    break
            if checkBit == 0:
                break
    return checkBit


##################################################################################################################
######### Main block of code #####################################################################################

#a = [1,2,3,4]
#b = 1
a,b = inputCon()
print(diffPair(a,b[1]))