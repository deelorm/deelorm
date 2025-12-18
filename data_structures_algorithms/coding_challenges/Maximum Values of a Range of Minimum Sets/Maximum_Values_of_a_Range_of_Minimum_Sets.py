
#Task -- Find the maximum value in each minimum set of values for a range of distinct artifact sizes
#First input line -- Array size e.g. {5}
#Second input line -- Array elements; space separated e.g. {1 2 3 4 5}

def artftMinMax(array1):
    maxVal = {}
    l = 0
    while l < len(array1):
        n = 0
        var2 = []
        while n < len(array1)-1:
            if l == 0:
                var2 = []
                for m in range(len(array1)):
                    var2.append(array1[m])
                break
            else:
                var = []
                if n+l+1 <= len(array1):
                    for m in range(n,n+l+1):
                        var.append(array1[m])
            if len(var) == l+1:
                var2.append(min(var))
            n += 1
        print(var2)
        maxVal[l+1] = max(var2)
        l += 1
    for itemVal in maxVal.values():
        print(itemVal, end=" ")
    print("")


#Queries user for array size
def inputLen():
    llen = int(input().strip())
    return llen


#Queries user for array elements 
def inputParam():
    listvar = input().strip().split(" ")
    listvar = list(map(int, listvar))
    return listvar


#Calls inputLen, inputParam functions & returns call values to inputCheck function
def inputInit():
    llen = inputLen()
    listvar = inputParam()
    cbit = inputCheck(llen, listvar)
    while not cbit:
        llen = inputLen()
        listvar = inputParam()
        cbit = inputCheck(llen, listvar)
    return listvar


#Checks the validity of user input against constraints
def inputCheck(llen, listvar):
    cbit = 1
    if llen < 1 or llen > pow(10,6):
        cbit = 0
    elif cbit:
        for l in range(len(listvar)):
            if listvar[l] < 0 or listvar[l] > pow(10,9):
                cbit = 0
                break
    return cbit


########################################################################################
########### Main Block of Code #########################################################

a = inputInit()
artftMinMax(a)





########################################################################################
############### Extra Test Cases #######################################################

#a = [2,6,1,12]
########################################################################################
