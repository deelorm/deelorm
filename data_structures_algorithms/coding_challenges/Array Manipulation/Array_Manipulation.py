
#Task --- Update array elements by a user given integer and return maximum value

# First line of user input [array length and number of test cases, space separated] e.g {5 2}
# Each test case should contain range of array indexes and number to be added at each index e.g {1 2 50}
# Uses a 1 index based array


#Iterates through a range of array indexes and adds user number to each index provided 
def arrayIter(array1, opDict):
    for k,v in opDict.items():
        index1 = v[0] - 1
        index2 = v[1]
        num = v[2]
        for i in range(index1, index2):
            if i <= len(array1)-1:
                array1[i] = array1[i] + num
    return max(array1)


#User input containing length of list & number of different input instances of list
def userArrOpp():
    userInput1 = input().strip().split(" ")
    userInput1 = list(map(int, userInput1))
    arrayLen = userInput1[0]
    opNum = userInput1[1]
    return arrayLen, opNum


#Queries for the different user test cases
def userOpQuery(opNum):
    valueOp = {}
    for i in range(opNum):
        userInput2 = input().strip().split(" ")
        userInput2 = list(map(int, userInput2))
        valueOp[i+1] = userInput2
    return valueOp


#Calls userArrOpp & userOpQuery functions and passes return values to userQueryCheck
def userQuery():
    arrayInit = []
    valueOp = {}
    vBit = 0

    arrayLen, opNum = userArrOpp()
    valueOp = userOpQuery(opNum)
    arrayInit = [ x-x for x in range(arrayLen) ]

    while not vBit:
        for value in valueOp.values():
            checkBit = userQueryCheck(arrayLen, opNum, value[0], value[1], value[2])
            if checkBit:
                vBit = 1
                break
            else:
                while not checkBit:
                                print("Re-enter all inputs ")
                                arrayLen, opNum = userArrOpp()
                                valueOp = userOpQuery(opNum)
                                break
    return arrayInit, valueOp


#Checks user input against constraints
def userQueryCheck(n, m, a, b, k):
    if n < 3 or n > pow(10,7):
        return 0
    elif m < 1 or m > pow(10,5)*2:
        return 0
    elif a < 1 or a > b:
        return 0
    elif b < a or b > n:
        return 0
    elif k < 0 or k > pow(10,9):
        return 0
    else:
        return 1



#############################################################################################
################### Main block of code ######################################################

arrayInit,testCase = userQuery()
print(arrayIter(arrayInit,testCase))






############################################################################################
############## Extra Test Cases ############################################################
#a = [0,0,0,0,0]
#b = {200:[1,2], 100:[2,5], 100:[4,5]}
#{400 500 200 200 100}
#{200, 300, 100, 200, 200 }
