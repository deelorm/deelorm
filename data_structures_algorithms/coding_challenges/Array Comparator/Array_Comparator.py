import copy

# Class to compare score values
class Item:
    def __init__(self,a1, b1):
        self.a1 = a1
        self.b1 = b1

# Compares score values
    def showDiff(self):
        if self.a1[1] < self.b1[1]:
            return -1
        elif self.a1[1] == self.b1[1]:
            return 0
        elif self.a1[1] > self.b1[1]:
            return 1

#Task -- return a sorted list of name-score pair arranging in descending order of score and ascending order of name if score is the same
def sortNamScor(array2d):  
    j = 0
    bCount = 1 
    item = {}
    objName = 'obj'
    itemName = ""
    while j <= len(array2d)-2:
        var1 = copy.copy(array2d[j])
        swapf = 0
        i = j+1
        while i <= len(array2d)-1:
            var2 = []
            var2 = copy.copy(array2d[i])

            for k in range(1, bCount+1):
                key = item.keys()
                if k not in key:
                    item[k] = objName + str(k)
                    itemName = item[k]
                    break

            itemName = Item(var1, var2)
            itemResult = itemName.showDiff()

            if itemResult == -1:
                var3 = []
                var3 = var1
                array2d[j] = var2
                array2d[i] = var3
                swapf = 1
            elif itemResult == 0:
                var3 = []
                if var1[0] > var2[0]:
                    var3 = var1
                    array2d[j] = var2
                    array2d[i] = var3
                    swapf = 1

            var1 = []
            var1 = copy.copy(array2d[i])
            i += 1
            j += 1
            bCount += 1
        if swapf == 0:
            break
        j = 0
    print("---Output---")
    for ele in range(len(array2d)):
        for ele1 in range(len(array2d[ele])):
            print(array2d[ele][ele1], end=" ")
        print("")
#    return array2d

# Number of user pair values
def inputLen():
    input1 = int(input().strip())
    return input1

# Queries for user name-score input 
def nameScore(input1):
    scoreName = []
    for k in range(input1):
        input2 = input().strip().split(" ")
        input2[0] = input2[0].lower()
        input2[1] = int(input2[1])
        scoreName.append(input2)
    return scoreName

# Calls inputLen & nameScore functions and passes return values to inputCheck
def inputCon():
    input1 = inputLen()
    scoreName = nameScore(input1)
    cbit = inputCheck(scoreName)
    while not cbit:
        input1 = inputLen()
        scoreName = nameScore(input1)
        cbit = inputCheck(scoreName)
    return scoreName

# Checks user input validity against constraints
def inputCheck(scoreName):
    cbit = 1
    if cbit:
        for k in range(len(scoreName)):
            for l in range(len(scoreName[k])):
                if l == 0:
                    continue
                if scoreName[k][l] < 0 or scoreName[k][l] > 1000:
                    cbit = 0
                    break 
            if cbit == 0:
                break
    return cbit

# Main block of code

#a = [['El',90], ['el1',91], ['el2',92], ['el3',93]] #91,90,92,93...91,92,90,93..91,92,93,90|
#a = [['El',90], ['el2',92], ['el3',93]]
#a = [[El,90], [el1,91], [el2,92], [el3,93]]

scoreName = inputCon()
sortNamScor(scoreName)      # 92 91 93 90.. 92 93 91 90 | 93 92 91 90

 
