
##Task -- Inplement the selection sort algorithm and return sorted array
#First input line -- User provide array elements; space separated e.g. {4 2 8 6}
#Sorts array using selection sort logic


#Implements slection sort function
def selSort(array1):
    temp = 0
    for i in range(len(array1)-1):
        j = i + 1
        swapped = 0
        temp = array1[i]
        swapIndex = -1
        while j <= len(array1)-1:
            if temp > array1[j]:
                temp = array1[j]
                swapped = 1
                swapIndex = j
            j += 1

        if temp < array1[i]:
            del array1[swapIndex]
            array1.insert(i, temp)

        if temp == array1[i] and not swapped:
            pass
    print("############ OUTPUT ##############")
    print(array1)
 

#Queries user for input
def inputQuery():
    input1 = input().strip().split(" ")
    input1 = list(map(int, input1))
    return input1

###########################################################################################################
####### Main code block ###################################################################################

userInput = inputQuery()
selSort(userInput)








'''
#print("2,1,4,3,2")
# 1,2,4,3,4 i=0 j=1
# 1,2,4,3,4 i=1 j=2
# 1,2,3,4,4 i=2 j=3
b = [3,1,4,6,9,2,12,5]
a = [2,1,4,3]
c = [2,4,3,1,2,7,5]
d = [2,1,11,4,4,0,7,3]
'''