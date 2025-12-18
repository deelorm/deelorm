
#Task is to match content of two strings such that one say str2 can be derived from str1 by deleting characters
# First line -- User string 1
# Second line -- User string 2

import copy 

# Compares two strings and returns matching string characters found in sequence
def stringMatch(str1, str2):
    str1= " ".join(str1)
    strArr1 = str1.split(" ")
    str2 = " ".join(str2)
    strArr2 = str2.split(" ")
    i = 0
    j = 0
    temp1 = copy.copy(strArr1).upper()
    temp2 = copy.copy(strArr2).upper()
    strArr3 = []

    while i <= len(temp1) - 1:

        while j <= len(temp2) - 1:
            if temp1[i] == temp2[j]:
                strArr3.append(temp1[i])
                if i+1 <= len(temp1) - 1 and j+1 <= len(temp2) - 1:
                    temp1 = temp1[i+1:]
                    temp2 = temp2[j+1:]
                    i =  -1
                    j = 0
                    break
                else:
                    if j == len(temp2) - 1:
                        temp2 = []
                        break
            elif j == len(temp2) - 1:
                if i+1 <= len(temp1) - 1:
                    temp1 = temp1[i+1:]
                    i = -1
                    j = 0
                    break
            else:
                j += 1
        if len(temp1) == 0 or len(temp2) == 0:
            break
        else:
           i += 1
    str3 = "".join(strArr3) 
    return str3


# Queries user for two string inputs
def userQuery():
    str1 = input().strip().upper()
    str2 = input().strip().upper()
    return str1,str2


# Call userQuery function and passes return values to userQueryCheck
def userQueryCon():
    str1, str2 = userQuery()
    checkBit = userQueryCheck(str1, str2)
    while not checkBit:
        str1, str2 = userQuery()
        checkBit = userQueryCheck(str1, str2)
    return str1, str2


# Checks validity of user input against constraints
def userQueryCheck(str1,str2):
    checkBit = 1
    if len(str1) != len(str2):
        checkBit = 0
    elif len(str1) < 1:
        checkBit = 0
    elif len(str2) > 5000:
        checkBit = 0
    
    if checkBit:
        return 1 
    else:
         return checkBit


#######################################################################################################
######## Main block of code ###########################################################################
#a = "abdcd"
#b = "cabed" 
#a = "HAARY"
#b = "SALLY"
#a = abdcd bdcd dcd cd  abd HARRY ARRY RRY  RY   Y    A
#b = cabed bed  ed  []         SALLY SALLY LLY LLY LLY

str1, str2 = userQueryCon()
print(stringMatch(str1,str2))













'''
    while i <= len(strArr1) - 1:       
        while j <= len(strArr2) - 1:
            if strArr1[i] == strArr2[j]:
                 strArr3.append(strArr1[i])
                 j = j + 1
                 break
            j += 1
        if j > len(strArr2) - 1:
            i = len(strArr1)
        else:
            i += 1 
    str3 = "".join(strArr3)
#    print(strArr3)
    return str3
'''
