
#Task -- find the number of consecutive multiples in a list based on a given ratio

#Returns the count of the number of pair multiples in a list considering duplicates given a user defined ratio==divisor
def multipleCount(array1, divisor):
    arrayLen = len(array1)
    temp1 = []
    multArr = []
    j = 0                  
    i = 0
    k = 0
    while j <= arrayLen-1: 
        i = j+1         
        temp1 = []                            
        while i <= arrayLen-1:       
            if array1[i] == array1[j]*divisor: 
                if len(temp1) == 0:
                    temp1.append(array1[j])
                    temp1.append(array1[i])
                    k = i+1

                    while k <= arrayLen-1:
                        flagmArr = 0
                        index1 = 0
                        index2 = 0
                        tempCount1 = 0
                        tempCount2 = 0
                        if array1[k] == array1[i]*divisor:
                            if len(temp1) == 2:
                                temp1.append(array1[k])
                                multArr.append(temp1)
                                index1 = k-i  
                                index2 = arrayLen-k-1  
                                if index1:
                                    tempCount1 = 0
                                    for q in range(i+1, k):
                                        temp2 = []
                                        if array1[q] == array1[i]:
                                            temp2.append(array1[j])
                                            temp2.append(array1[q])
                                            temp2.append(array1[k])
                                            multArr.append(temp2)
                                            tempCount1 += 1
                                if index2:
                                    tempCount2 = 0
                                    for q in range(k+1, arrayLen):
                                        temp3 = []
                                        if array1[q] == array1[k]:
                                            temp3.append(array1[j])
                                            temp3.append(array1[i])
                                            temp3.append(array1[q])
                                            multArr.append(temp3)
                                            tempCount2 += 1
                                    if tempCount2:
                                        var = tempCount2 * (tempCount1)
                                        for q in range(var):
                                            temp4 = []
                                            temp4.append(array1[j])
                                            temp4.append(array1[i])
                                            temp4.append(array1[k])
                                            print(temp4)
                                            multArr.append(temp4)
                                    break
                        if k == arrayLen-1 and array1[k] != array1[i]*divisor: #
                            temp1 = []
                            break
                        k += 1
            if k == len(array1)-1:
                break
            i += 1
        j += 1
    print(multArr)
    return len(multArr)


#Queries user for array length, integer ratio & elements of arrays
def inputVar():
    input1 = input().strip().split(" ")
    input1 = list(map(int,input1))

    input2 = input().strip().split(" ")
    input2 = list(map(int,input2))
    return input1, input2


#Calls inputVar function and returns call value to inputCheck function
def inputCon():
    input1, input2 = inputVar()
    checkBit = inputCheck(input1, input2)
    while(not checkBit):
        print("Re-enter Inputs: ")
        input1, input2 = inputVar()
        checkBit = inputCheck(input1, input2)
    return  input2, input1[1]


#Checks validity of user input against constraints
def inputCheck(input1, input2):
    checkBit = 1
    if input1[0] < 1 or input1[0] > pow(10,5):
        checkBit = 0
    elif input1[1] < 1 or input1[1] > pow(10,9):
        checkBit = 0 
    elif checkBit:
        for i in range(input1[0]):
            if input2[i] > pow(10,9):
                checkBit = 0
                break
    return checkBit
       

#########################################################################################
################ MAIN BLOCK OF CODE #####################################################

array1, divisor = inputCon()
print(multipleCount(array1,divisor))













#########################################################################################
########### EXTRA TEST CASES ############################################################
#########################################################################################
# 1 3 9 9 27 81
#a = [1,2,2,4]
#b = 2
#a1 = [1,3,9,9,27,81]
#b1 = 3
#a3 = [1,5,5,25,125]
#b3 = 5
#########################################################################################















##################################################################################
################## IGNORE    #####################################################
################ CODE BLOCK ######################################################

#    while j+1 <= arrayLen-1 and j+2 <= arrayLen-1:
#        flagTemp1 = 0 
#        flagTemp2 = 0
#        if array1[j+1] == array1[j] * divisor:
#            temp1.append(array1[j])
#            temp1.append(array1[j+1])
#            index1 = j+1
#            flagTemp1 = 1

#        if array1[j+2] == array1[j+1] * divisor:
#            if flagTemp1:
#                temp1.append(array1[j+2])
#                index2 = j+2
#                flagTemp2 = 1

#       if flagTemp1 and flagTemp2:
#            multArr.append(temp1)
####################################################################################