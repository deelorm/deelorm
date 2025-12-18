
#Task return number of toys that can be bought given a list of them with prices and a given amount to spend
#First input line -- Total number of items and given amount to spend; space separated e.g. {5 16}
#Second input line -- Prices of items represented by array elements; space separated e.g. {2 3 6 9 11}

#Implements bubble sort function
def sort(array1):
    j = 0
    while j <= len(array1)-2:
        var1 = array1[j]
        i = j+1
        swapFlg = 0
        while i <= len(array1)-1:
            var2 = array1[i]
            if var1 > var2:
                var3 = var1
                array1[i-1] = var2
                array1[i] = var3
                swapFlg = 1
            var1 = array1[i]
            i += 1
        if swapFlg == 0:
            break
        j = 0
    return array1


#Returns maximum number of toys that can be bought with a given amount
def maxToys(array1, expen):
    array1 = sort(array1)
    price = 0
    toyCount = 0
    j = 0
    while j <= len(array1)-1:
        initCost = price + array1[j]
        if initCost <= expen:
            price += array1[j]
            toyCount += 1
        else:
            break
        j += 1
    return toyCount


#Queries user for array size and amount available to spend
def inputParam():
    sizeTgt = input().strip().split(" ")
    sizeTgt = list(map(int,sizeTgt))
    return sizeTgt


#Queries user for array element values (prices of items)
def inputList():
    listCst = input().strip().split(" ")
    listCst = list(map(int,listCst))
    return listCst


#Calls inputParam, inputList functions and returns call values to the inputCheck function
def inputCon():
    sizeTgt = inputParam()
    listCst = inputList()
    cbit = inputCheck(sizeTgt, listCst)
    while not cbit:
        sizeTgt = inputParam()
        listCst = inputList()
        cbit = inputCheck(sizeTgt, listCst)
    return listCst,sizeTgt


#Checks the validity of user inputs against constraints
def inputCheck(sizeTgt, listCst):
    cbit = 1
    if len(listCst) != sizeTgt[0]:
        cbit = 0
    elif sizeTgt[0] < 1 or sizeTgt[0] > pow(10,5):
        cbit = 0
    elif sizeTgt[1] < 1 or sizeTgt[1] > pow(10,9):
        cbit = 0
    elif cbit:
        for i in range(len(listCst)):
            if listCst[i] < 1 or listCst[i] > pow(10,9):
                cbit = 0
                break
    return cbit


####################################################################################################
######### MAIN BLOCK OF CODE #######################################################################

a,b = inputCon()
print(maxToys(a,b[1]))





########################################################################################################
########### EXTRA TEST CASES ###########################################################################
#a = [6,4,1,2,3,2,1]
#print(sort(a))
#maxToys(a,7)
#a = [1,2,3,4]
########################################################################################################