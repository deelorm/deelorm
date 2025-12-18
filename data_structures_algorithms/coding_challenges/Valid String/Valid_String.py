
#Task -- Check if a string is valid if the number of occurence of all characters are the same after the removal of element index 1
# Input -- user string e.g {aaabbcc} returns YES, {aabbcdac} returns NO

import copy
import re

# Returns YES, if string char count is equal for all  char is the same after removal of str chr at index 1, otherwise it returns NO
def isValid(str1): 
    str2 = []
    strCount = {}
    
    for j in range(len(str1)):
        if j != 1:
            str2.append(str1[j])
    str2 = "".join(str2).lower()

    for i in range(len(str2)):
        strKeys = strCount.keys()
        if str2[i] in strKeys:
            strCount[str2[i]] += 1 
        else:
            strCount[str2[i]] = 1

#    print(strCount)
#    print(str2)
    valInit = strCount[str2[0]]
    stringIndic = "YES"
    for value in strCount.values():
        if value != valInit:
            stringIndic = "NO"
            break
    return stringIndic


# Take user string input and returns value to inputQueryCheck
def inputQuery():
    str1 = input().strip()
    checkBit = inputQueryCheck(str1)
    while not checkBit:
        print("Re-enter input string: ")
        str1 = input().strip()
        checkBit = inputQueryCheck(str1)
    return str1


# Checks validity of user input against constraints
def inputQueryCheck(str1):
    checkBit = 1
    strPattern = re.compile(r"[^a-z]")
    strMatch = strPattern.findall(str1)
    if len(str1) < 1 or len(str1) > pow(10,5):
        checkBit = 0
    elif len(strMatch) != 0:
        checkBit = 0
    return checkBit


############################################################################################################
############## Main block of code ##########################################################################
#a = "aabbccdda"
a = inputQuery()
print(isValid(a))





    


