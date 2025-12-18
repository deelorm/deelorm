#Task -- Returns number of repetitions needed such that elements have higher/equal succeeding values
#First input line -- Integer number representing number of elements e.g. {2}
#Second input line -- Values of elements of an array; space separated  e.g. {2 1 3 4 5}

import copy 

#Sorts list such that each elements succeeding value has a higher/equal value than previous one & returns no. of iterations needed to complete task
def ttlSpan(array1):
    array2 = copy.copy(array1)
    l = 0
    dcount = 0
    while l < len(array2):
        n = 0 
        var = []
        contntf = 0
        while n < len(array2)-1:
            if n+1 < len(array2):
                if array2[n] < array2[n+1]:
                    var.append(array2[n+1])
                    contntf += 1
            n += 1
        if contntf == 0:
            break
        for m in range(len(var)):
            array2.remove(var[m])
        dcount += 1
        l = 0
    return dcount


#Queries user for length of input list
def inputLen():
    llen = int(input().strip())
    return llen


#Queries user for input list data
def inputParam():
    var = input().strip().split(" ")
    var = list(map(int, var))
    return var


#Calls inputLen & inputParam functions and passes return values to inputCheck function
def inputInit():
    llen = inputLen()
    var = inputParam()
    cbit = inputCheck(llen, var)
    while not cbit:
        llen = inputLen()
        var = inputParam()
        cbit = inputCheck(llen, var)
    return var

#Checks validity of user input against constraints
def inputCheck(llen, var):
    cbit = 1
    if llen < 1 or cbit > pow(10,5):
        cbit = 0
    elif cbit:
        for l in range(len(var)):
            if var[l] < 0 or var[l] > pow(10,9):
                cbit = 0
                break
    return cbit


########################################################################################################
########### Main Block of Code #########################################################################

c = inputInit()
print(ttlSpan(c))



##Extra test data
#a = [6,5,8,4,7,10,9]
#a = [6,5,8,4,7,10,9]
#b = [3,6,2,7,5]