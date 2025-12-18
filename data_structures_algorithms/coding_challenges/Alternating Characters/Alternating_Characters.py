import copy

# Provide minimum number of deletions needed to produce a string with non-matching alternating characters
def alterStrNum(str1):
    str2 = copy.copy(str1).upper()
    str2 = " ".join(str2)
    str2= str2.split(" ")
    delCount = 0
    j = 0
    while j <= len(str2)-2:
        if j+1 <= len(str2)-1:
            if str2[j] == str2[j+1]:
                del str2[j]
                delCount += 1
            j += 1
    str2 = "".join(str2)
    return delCount

# Number of user test cases
def queryOccrr():
    qNum = int(input().strip())
    return qNum

# User input string for each test case
def inputQuery(qNum):
    queries = {}
    for j in range(qNum):
        str1 = input().strip()
        queries[j+1] = str1
    return queries

# Calls queryOccrr & inputQuery funtions and passes return to inputQueryCheck function
def inputQueryCon():
    qNum = queryOccrr()
    queries = inputQuery(qNum)
    checkBit = inputQueryCheck(qNum, queries)
    while not checkBit:
        qNum = queryOccrr()
        queries = inputQuery()
        checkBit = inputQueryCheck(qNum, queries)
    return qNum, queries

# Checks the validity of user input against constraints
def inputQueryCheck(qNum, queries):
    checkBit = 1
    if qNum < 1 or qNum > 10:
        checkBit = 0
    elif checkBit:
        for v in queries.values():
            if len(v) < 1 or len(v) > pow(10,5):
                checkBit = 0
                break 
    return checkBit

# Main block of code
#a = "AABAAB"
a, q = inputQueryCon()
for v in q.values():
    print(alterStrNum(v))
