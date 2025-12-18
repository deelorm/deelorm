import copy

# Checks the number of occurence of "a" in a string
def calculateA(var, n):
    var = var.lower()
    newVar = []
    aCount = 0
    i = 0
    while i <= n-1:
        varCount = 0
        for j in var:
            if len(newVar) < n:
                newVar.append(j)
                varCount += 1
            else:
                break
        i += varCount
    for k in range(len(newVar)):
        if newVar[k] == "a":
            aCount += 1
    return aCount

# Queries for user Input -- First line contains string & second line takes length of user input
def userQuery():
    checkBit = 0
    userString = input().strip()
    n = int(input().strip())
    checkBit = userCheck(userString, n)
    if checkBit == 1:
        pass
    else:
        while not checkBit:
            userString = input().strip()
            n = int(input().strip())
            checkBit = userCheck(userString, n)

    return userString, n


#Checks validity of provided user input against constraints 
def userCheck(var, n):
    if len(var) != n:
        return 0
    elif len(var) < 1 or len(var) > 100:
        return 0
    elif n < 1 or n > pow(10,12):
        return 0
    else:
        return 1


# Main block for function call
#userInput = "Abab"
userString, n = userQuery()
print(calculateA(userString, n))

