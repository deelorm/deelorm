
#Task -- finding matching pair of square brackets, paranthesis & curly brackets [] () {}
# First input line -- number of testcases
# Second input line -- string values for accompanying testcases
# e.g of input ({[]}), returns YES, ({)} returns NO

# Returns appropriate match for bracket/paran/curly
def bracMatch(bracstr):
    if bracstr == '[':
        return ']'
    elif bracstr == '{':
        return '}'
    elif bracstr == '(':
        return ')'

# Compares a string of paran/brac/curly brackets and return YES if each pair of paran/curly/brac is macthed, otherwise NO
def bracParaMatch(strval):
    if len(strval) % 2 == 1:
        return "NO"
    else:
        mid = int(len(strval)/2)
        sec1 = strval[:mid]
        sec2 = strval[mid:]
        sec2 = sec2[::-1]
        matchIndic = 0
        l = 0
        while l < len(sec2) and l < len(sec1):
            matchPair = bracMatch(sec1[l])
            if sec2[l] == matchPair:
                pass
            else:
                matchIndic = 1
                break
            l += 1
        if matchIndic:
            return "NO"
        else:
            return "YES"

# Number of user testcases
def strSpan():
    strlen = int(input().strip())
    return strlen

# User string for each test case
def strInput(strlen):
    strdict = {}
    for l in range(strlen):
        strA = input().strip()
        strdict[l+1] = strA
    return strdict

# Calls Strspan & strInit functions and passes return values to inputCheck
def strInit():
    strlen = strSpan()
    strdict = strInput(strlen)
    cbit = inputCheck(strlen, strdict)
    while not cbit:
        strlen = strSpan()
        strdict = strInput(strlen)
        cbit = inputCheck(strlen, strdict)
    return strdict

# Checks validity of input strings against constraint
def inputCheck(strlen, strdict):
    pairstr = ['{','}','[',']','{','}']
    cbit = 1
    if strlen < 1 or strlen > pow(10,3):
        cbit = 0
        return cbit
    elif cbit:
        values = list(strdict.values())
        for l in range(len(values)):
            if len(values[l]) < 1 or len(values[l]) > pow(10,3):
                cbit = 0
                break
                strval = values[l]
                for n in range(len(strval)):
                    if strval[n] not in pairstr:
                        cbit = 0
                        break
    return cbit

##############################################################################################################
# Main block of code 
dicta = strInit()
strval = list(dicta.values())
for n in range(len(strval)):
    print(bracParaMatch(strval[n]))
    
#a = "{[[{()}]]}"
#b = "{[(])}"
#print(bracParaMatch(b))