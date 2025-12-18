#Task -- sorts an array using merge sort function
#First input line -- user provide array elements; space separated e.g. {5 4 3 2 1}

import copy

#Divides two arrays into atomic (indivisible) size
def nsort(array1):
    n = len(array1)
    if n == 1:
        return array1
    else:
        index1 = int(n/2)
        var1 = nsort(array1[:index1])
        var2 = nsort(array1[index1:n])
    return mergeArray(var1, var2) 

#Merges two array
def mergeArray(a1,b1):
    c1 = []
    j = 0
    i = 0

    if a1 == 'None' or b1 == 'None':
        if a1 == 'None':
            return b1
        else:
            return a1
    else:
        while len(a1) != 0 and len(b1) != 0:
            if a1[j] < b1[i]:
                c1.append(a1[j])
                del a1[0]
            else:
                c1.append(b1[i])
                del b1[0]

        while len(a1) != 0:
            for j in range(len(a1)):
                c1.append(a1[j])
            break
        while len(b1) != 0:
            for i in range(len(b1)):
                c1.append(b1[i])
            break
    return c1

#Queries user for input array
def userInput():
    array1 = input().strip().split(" ")
    array1 = list(map(int,array1))
    return array1


##################################################################################
######## MAIN BLOCK OF CODE ######################################################  

#array1 = [7,6,4,2]

#array1 = userInput()

array1 = [3,2,1,4]
print('List before', array1)
print('List after', nsort(array1))
