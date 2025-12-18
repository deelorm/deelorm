
#Task --- Return number of swaps required to sort an array using bubble sort
# First line -- length of array e.g {5}
# Second line -- array, arr to be considered, space separated e.g {5 6 7 2 3}
# e.g 

# Bubble Sort function
def bubbleSort(array1):
    numSwap = 0
    j = 0
    while j <= len(array1)-2:
        var1 = array1[j]
        i = j + 1
        swapFlg = 0
        while i <= len(array1)-1:
            var2 = array1[i]
            if var1 > var2:
                var3 = var1
                array1[i-1] = var2
                array1[i] = var3
                numSwap += 1
                swapFlg = 1
            var1 = array1[i]
            i += 1
        if swapFlg == 0:
            break
        j = 0
    
    print("Array is sorted in", numSwap)
    print("First element:", array1[0])
    print("Last element:", array1[-1])
    print(array1)


# Query user for length of array
def inputLen():
    listSize = int(input().strip())
    return listSize


# Query user for arrray input 
def inputList():
    input1 = input().strip().split(" ")
    input1 = list(map(int,input1))
    return input1

# Calls inputLen & inputList functions & passes return values to inputCheck
def inputCon():
    listSize = inputLen()
    input1 = inputList()
    checkBit = inputCheck(listSize, input1)
    while not checkBit:
        listSize = inputLen()
        input1 = inputList()
        checkBit = inputCheck(listSize, input1)
    return input1


# Checks user inputs against constraints
def inputCheck(listSize, input1):
    checkBit = 1
    if len(input1) != listSize:
        checkBit = 0
    elif listSize < 2 or listSize > 600:
        checkBit = 0
    elif checkBit:
        for i in range(len(input1)):
            if input1[i] < 1 or input1[i] > pow(10,6)*2:
                checkBit = 0
                break
    return checkBit

###################################################################################################################
# Main block of code
###################################################################################################################

#a = [6,4,1]
arr = inputCon()
bubbleSort(arr)
         

