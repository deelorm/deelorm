
#Task --- Check if string b can be derived from string a and return YES or NO depending on result
# String value B must be all upper caps
# First input line -- number of testcase e.g. {1}
# Second input line -- string value A e.g {abcdefg}
# Third input line -- string value B e.g {ABCD}
import re


# Checks if strb can be derived from stra 
def strMatch(stra, strb):
    if strb not in stra.upper():
        return "NO"
    else:
        strvar = [] 
        for l in range(len(stra)):
            if stra[l].upper() in strb:
                strvar.append(stra[l])

        for n in range(len(strvar)):
            if strvar[n].islower():
                strvar[n] = strvar[n].upper()
        strvar = "".join(strvar)
        if strvar == strb:
            return "YES"
        else:
            return "NO"
 

# Queries user for number of test cases
def testCases():
    tcase = int(input().strip())
    return tcase


# Queries user for input strings for tcase number of testcases
def inputParam(tcase):
    tdict = {}
    for l in range(tcase):
        var = []
        stra = input().strip().upper()
        strb = input().strip().upper()
        var.append(stra)
        var.append(strb)
        tdict[l+1] = var
    return tdict


# Calls testCases & inputParam functions and passes return values to inputCheck
def inputInit():
    tcase = testCases()
    tdict = inputParam(tcase)
    cbit = inputCheck(tcase, tdict)

    while not cbit:
        tcase = testCases()
        tdict = inputParam(tcase)
        cbit = inputCheck(tcase, tdict)

    return tdict


# Check validity of input against constraints
def inputCheck(tcase, tdict):
    cbit = 1
    strrega = re.compile(r"[^a-zA-Z]")
    strregb = re.compile(r"[^A-Z]")
    if tcase < 1 or tcase > 10:
        cbit = 0
    elif cbit:
        values = list(tdict.values())
        for l in range(len(values)):
            regmata = strrega.findall(values[l][0])
            regmatb = strregb.findall(values[l][1])
            if regmata or regmatb:
                cbit = 0
                break
            else:
                for m in range(len(values[l])):
                    if len(values[l][m]) < 1 or len(values[l][m]) > 1000:
                        cbit = 0
                        break 
    return cbit


#######################################################################################################
####### Main Code Block ###############################################################################

a = "jaBCd"
c = "bcd"
b = "ABC"

tdict = inputInit()
for value in tdict.values():
    print(strMatch(value[0], value[1]))