
#Task -- Hop between valid "0" user inputs until end of array; a hop of 1 is avoided.
#User input consists of a list of 0's & 1's
# Just single (i+1) and double (i+2) hops are allowed.
#First line input -- Integer number representing length of list e.g. {6}
#Second line input -- Values of list elements; space separated e.g {0 1 0 0 0 0}

#Returns number of hops between user inputs "0 & 1"s, "0" is considered right while "1" is avoided
def hopGame(array1):
    i = 0
    hopCount = 0
    while i <= (len(array1)-1):
        hop1 = i + 1
        hop2 = i + 2
        loopCount1 = 0
        loopCount2 = 0
        if i == len(array1)-1:
            break
        if hop2 <= len(array1) - 1:
            if array1[hop2] == 0:
                loopCount2 = 2
        if hop1 <= len(array1) - 1:
            if array1[hop1] == 0:
                loopCount1 = 1            
        if loopCount2:
            i += loopCount2
        elif loopCount1:
            i += loopCount1
        hopCount += 1
    return hopCount

#Queries user input and calls user inpuCheck function (user has 5 chances to input right data after initial chance i.e 1+5)
def userInput():
    n = int(input().strip())
    N = input().strip().split(" ")
    N = list(map(int,N))
    userVal = userInputCheck(N, n)
    for i in range(5):
        if userVal == "Check":
            n = int(input().strip())
            N = input().strip().split(" ")
            N = list(map(int,N))
            userVal = userInputCheck(N, n)
        else:
            return N
        if i == 4 and userVal == "Check":
            return []
        elif i == 4 and userVal == "Uncheck":
            return N

#Function to check if user input is within constraint
def userInputCheck(a, n):
    ret = "Uncheck"
    if n < 2 or n > 100:
        ret = "Check"
    elif len(a) < n:
        ret = "Check"
    elif a[n-1] == 1 or a[0] == 1:
        ret = "Check"
    elif len(a) == n:
        for i in range(n):
            if i+1 <= n-1:
                if a[i] == 1 and a[i+1] == 1:
                    ret = "Check"
    return ret


############################################################################################
####### MAIN BLOCK OF CODE #################################################################

b = userInput()
print(hopGame(b))


##Extra test cases
#a = [0,1,0,0,1,0]
#b = [0,1,0,0,1,0,0,0,0]
#c = [0,1,0,0,1,0,0]
#print(b)
#print(c)

# a=[0 1 0 0 1 0]
#b = [0,1,0,0,1,0,0,0,0]
#i = 5 c = 3