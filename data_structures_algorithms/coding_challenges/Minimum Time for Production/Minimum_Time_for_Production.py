#Task -- provide the minimum time required to hit a target production given a number of machines
# First input line -- Machine capacity and target prod number; space separated e.g {3 10}
# Second input line -- Various values for machine capacity e.g. space separated {2 3 2}


#Returns minimun time required to hit a target production
def minProdTime(machSize, mparam):
    tCount = 0
    j = 1
    while tCount != mparam[1]:
        for i in range(mparam[0]):
            if j % machSize[i] == 0 and tCount != mparam[1]:
                tCount += 1
        if tCount == mparam[1]:
           break
        j += 1
    return j


#Queries user for number of machines and target production
def inputParam():
    mparam = input().strip().split(" ")
    mparam = list(map(int,mparam))
    return mparam


#Queries user for machine production capacities
def unitSize():
    machSize = input().strip().split(" ")
    machSize = list(map(int,machSize))
    return machSize


#Calls inputParam & unitSize and returns call values to inputCheck
def inputCon():
    mparam = inputParam()
    machSize = unitSize()
    checkBit = inputCheck(mparam, machSize)
    while not checkBit:
        mparam = inputParam()
        machSize = unitSize()
        checkBit = inputCheck(mparam, machSize)
    return machSize, mparam


#Checks validity of user input against constraint
def inputCheck(mparam, machSize):
    checkBit = 1
    if len(machSize) != mparam[0]:
        checkBit = 0 
    elif mparam[0] < 1 or mparam[0] > pow(10,5):
        checkBit = 0
    elif mparam[1] < 1 or mparam[1] > pow(10,9):
        checkBit = 0 
    elif checkBit:
        for i in range(len(machSize)):
            if machSize[i] < 1 or machSize[i] > pow(10,9):
                checkBit = 0
                break
    return checkBit


#################################################################################################
##### Main Code block ###########################################################################


a,b = inputCon()
print(minProdTime(a,b))


# Extra test cases
#a = [2,3,2]
#b = [3,10]
# 2 3 2  10    1 2 3 4 5 6
