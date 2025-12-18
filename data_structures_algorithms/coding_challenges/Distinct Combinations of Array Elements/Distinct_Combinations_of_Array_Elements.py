#Task -- find an array[i,j,k] using three arrays a,b,c such that a[indx] <= b[indx] and b[ele] >= c[indx]

# First line -- length of all 3 arrays, space separated 
# Next n=3 lines -- values of all arrays

import copy


#Provides arrays pairs arr[i,j,k ] such that a[i] <= b[ij] and b[ele] >= c[k]
def arrayComb(array1, array2, array3):
    result = []
    var1 = []

    for i in range(len(array1)):
        var = []
        j = 0
        while j <= len(array2)-1:
            if array1[i] <= array2[j]:
                var.append(array1[i])
                var.append(array2[j])
                k = 0
                while k <= len(array3)-1:
                    if array2[j] >= array3[k]:
                        var.append(array3[k])
                        var1 = copy.copy(var)
                        result.append(var1)
                    if len(var) == 3:
                        var.pop()
                    k += 1               
            var = []
            j += 1
    result = compareArray(result)
    return len(result)
#    for l in range(len(result)):
#       print(result[l], end=" ")
#   print("")


#Iterates through array to remove duplicate elements
def compareArray(result):
    i = 0
    while i <= len(result)-2:
        var = copy.copy(result[i])
        j = i + 1
        while j <= len(result)-1:
            if var == result[j]:
                del result[j]
                j -= 1
            j += 1
        i += 1
    return result


#Queries user for length of arrays 
def inputLen():
    alen = input().strip().split(" ")
    alen = list(map(int,alen))
    return alen


#Queries user for values of all 3 arrays
def inputVar(alen):
    array1 = []
    for i in range(len(alen)):
        input1 = input().strip().split(" ")
        input1 = list(map(int, input1))
        array1.append(input1)
    return array1


#Calls inputLen, inputVar and returns call values to inputCheck function
def inputCon():
    alen = inputLen()
    array1 = inputVar(alen)
    checkBit = inputCheck(alen, array1)
    while not checkBit:
        alen = inputLen()
        array1 = inputVar(alen)
        checkBit = inputCheck(alen, array1)
    return array1


#Checks validity of user input against constraints
def inputCheck(alen, array1):
    checkBit = 1 
    if checkBit:
        for i in range(len(alen)):
            if alen[i] < 1 or alen[i] > pow(10,5):
                checkBit = 0
                break
    elif checkBit:
        for j in range(len(array1)):
            var = array1[j]
            for i in range(len(var)):
                if var[i] < 1 or var[i] > pow(10,8):
                      checkBit = 0
                      break
    return checkBit


#############################################################################################################
######### Main Block of Code ################################################################################


arrayNest = inputCon()
print(arrayComb(arrayNest[0], arrayNest[1], arrayNest[2]))

























# Extra test cases
#b = [3,6]
#c = [4,6,9]
#a = [[3,6,4],[3,6,6],[3,6,4],[5,6,4]]
#b =[[1, 2, 1], [1, 2, 2], [1, 3, 1], [1, 3, 2], [1, 3, 3], [1, 3, 1], [1, 3, 2], [1, 3, 3]]
#a = [1,2,3,4,5]
#b = [11,12,13,14,15]
#c = [6,7,8,9,10]
#print(arrayComb(a, b, c))
#print(compareArray(b))
#arrayComb(a,b,c)