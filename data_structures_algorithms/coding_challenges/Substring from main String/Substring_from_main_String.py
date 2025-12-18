import math as f 

# Task -- Compares and returns the count number of substrings of a string that match a criteria
# C1 -- All single chars are considered a match
# C2 -- All even number substrings should have same characters
# C3 -- All odd number substrings should differ by just string char of index 1
# First line of input -- String length
# Second line of input -- String input

# Compares string to determine match: if string length is even then all string char must be the same to match,
# If odd, then must differ by just string character of index 1
# Return 1 for a string match, otherwise 0

def stringIndic(str1):
    stringBit = 1
    if len(str1) % 2 == 0:
        if stringBit:
            for i in range(len(str1)):
                if str1[0] != str1[i]:
                    stringBit = 0
                    break
    elif len(str1) % 2 == 1:
        if len(str1) == 1:
            stringBit = 1
        elif stringBit:
            midChart = f.ceil(len(str1)/2) - 1
            for i in range(len(str1)):
                if str1[0] != str1[i]:
                    if i != midChart:
                        stringBit = 0
                    else:
                        stringBit = 1

    return stringBit
# 0:2 ab 1:3 ba 2:4 !!aa  3:5 ad 4:6 da  abaada
# 0:3 !!aba 1:4 baa  2:5 aad 3:6 !!ada
# 0:4 abaa 1:5 baad 2:6 aada
# 0:5 abaad 1:6 baada
# 0:6 abaada


# Iterates through string and calls stringIndic function with substring of len {2,3...len(str)} and returns matching string count
def subStringGen(str1):
    subList = []
    strLen = len(str1)
    h = 0
    while h <= strLen - 1:
        for i in range(strLen):
            if h == 0:
                subList.append(str1[i])
            else: 
                temp = str1[i:h+i+1]
                print(temp)
                stringCheck = 0
                if len(temp) == h + 1:
#                    temp = str1[i:h+i+1]
                    stringCheck = stringIndic(temp)
                    if stringCheck:
                        subList.append(temp)
                else:
                    break
        h += 1
#    print(subList)
    return len(subList)


# Queries user for string length and stirng value, and returns values to userQueryCheck
def userQuery():
    strLen = int(input().strip())
    str1 = input().strip()
    checkBit = userQueryCheck(strLen, str1)
    while(not checkBit):
        print("Print new set of inputs: ")
        strLen = int(input().strip())
        str1 = input().strip()
        checkBit = userQueryCheck(strLen, str1)
    return strLen, str1


# Checks validity of user input against constraints
def userQueryCheck(strLen, str1):
    checkBit = 1
    if strLen < 1 or strLen > pow(10,6):
        checkBit = 0
    elif strLen != len(str1):
        checkBit = 0
    return checkBit


###############################################################################
######### Main Block of Code ##################################################
#a = "abaada"
n, arr = userQuery()
print(subStringGen(arr))
#print(stringIndic('aaaa'))

