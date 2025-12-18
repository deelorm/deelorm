
# Task #1 if '1' append element d, if #2 delete first occurence of element d,  #3 Check d frequency (if it occurs twice) of element in form [{1223}, d]
#For operation input line, first value depicts operation kind and second value states the value
#First input line -- No. of operations e.g. {3}
#Next n input lines -- for operation say 3 e.g. {1 2\n} {1 3\n} {3 2\n}; space separated inputs on each line

#Performs a given number of operations with given inputs and operation type
def userOperation(array1):
    op = array1[0]
    ele = array1[1]
    array2 = []

    for j in range(len(array1)):
        op = array1[j][0]
        ele = array1[j][1]
        if op == 1:
            array2.append(ele)
        if op == 2:
            if ele in array2:
                array2.remove(ele)
        if op == 3:
            opdict = {}
            for i in range(len(array2)):
                eleKeys = opdict.keys()
                if array2[i] in eleKeys:
                    opdict[array2[i]] += 1
                else:
                    opdict[array2[i]] = 1
            dictValue = opdict.values()
            for k,v in opdict.items():
                if k == ele:
                    if k == ele and v == 2:
                        print(1)
                    else:
                        print(0)
    print("------------Final Array------------")
    print(array2)


#Queries user for number of operations to be performed
def userInput1():
    opNum = int(input().strip())
    return opNum


#Queries user for operation and element values 
def userInput2(opNum):
    opArray = []
    for j in range(opNum):
        input1 = input().strip().split(" ")
        input1 = list(map(int, input1))
        opArray.append(input1)
    return opArray


#Calls userInput1, userInput2 functions and return function call values to userInputCheck
def userInputCon():
    opNum = userInput1()
    opArray = userInput2(opNum)
    checkBit = userInputCheck(opNum, opArray)
    while not checkBit:
        opNum = userInput1()
        opArray = userInput2()
        checkBit = userInputCheck(opNum, opArray)
    return opArray


#Checks validity of user input against constraints
def userInputCheck(opNum, opArray):
    checkBit = 1
    if opNum < 1 or opNum > pow(10,5):
        checkBit = 0
    elif True:
        pass
        for j in range(len(opArray)):
            if opArray[j][0] < 1 or opArray[j][0] > pow(10,9):
                checkBit = 0
                break
            if opArray[j][1] < 1 or opArray[j][1] > pow(10,9):
                checkBit = 0
                break
    return checkBit


####################################################################################################################
############# Main Block of Code ###################################################################################
#a = [[1,2], [1,2], [1,2], [2,2], [3,2]]
a = userInputCon()
userOperation(a)
