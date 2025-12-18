
import math as f

#Task --- Find number of alerts received from an entity given a list of expenditures and number of history expenditures to use for determination
# Calculates median of history expenditures
# If day spend is greater or equal to twice the median history expenditure, notify user via an alert
#e.g expenditure [2 ,3, 4, 5, 6, 7, 8] & if h, no.of history expenditure = 3 consider array indexes {1 2 3} 

# Returns number of alerts sent out for a given integer for history length and list of expenditures

def alertFreq(expenArray, histLen):

    alertCount = 0
    median = 0
    dayExpen = 0   #[1 3 4 5 6 7]
    j = 0
    while j <= len(expenArray)-1:
        if j < histLen:
            j += 1
            continue

#        if j-histLen < 0 and j == len(expenArray)-1:
#            print("Not enough history data")
#            return alertCount

        if histLen % 2 == 1:
            mid = f.ceil(histLen/2)
            median = expenArray[j-mid]
        else:
            mid = histLen/2
            median = int((expenArray[j-mid] + expenArray[j-mid-1])/2)
            
        dayExpen = expenArray[j]
        if dayExpen >= 2*median:
            alertCount += 1

        if j == len(expenArray)-1:
            return alertCount
#        print(j, median, alertCount)
#        print(j)
        j += 1

# Number of transactions & history length to consider 
def inputParam():
    input1 = input().strip().split(" ")
    input1 = list(map(int,input1))
    return input1


# A list of past expenditures
def inputExpen():
    expen = input().strip().split(" ")
    expen = list(map(int,expen))
    return expen


# Calls inputParam & inputExpen functions and passes return values to inputCheck
def inputCon():
    input1 = inputParam()
    expen = inputExpen()
    cbit = inputCheck(expen, input1)
    while not cbit:
        input1 = inputParam()
        expen = inputExpen()
        cbit = inputCheck(expen, input1)
    return expen, input1


# Checks user input against constraint
def inputCheck(expen, input1):
    cbit = 1
    if len(expen) != input1[0]:
        cbit = 0
    elif input1[0] < 1 or input1[0] > pow(10,5)*2:
        cbit = 0
    elif input1[1] < 1 or input1[1] > input1[0]:
        cbit = 0
    elif cbit:
        for i in range(len(expen)):
            if expen[i] < 0 or expen[i] > 200:
                cbit = 0
                break
    return cbit


# Main block of code
#expen = [10,20,30,40,50]
#h = 3
#expen, h = inputCon()

expen, h = inputCon()
print(alertFreq(expen, h[1]))