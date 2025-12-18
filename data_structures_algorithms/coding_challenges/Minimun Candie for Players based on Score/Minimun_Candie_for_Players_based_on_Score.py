
# Task -- Distribute/Find minimum candies using their score..e.g. if player1 has higher rating than player2, player2 receives more candie than player1
# First input -- Number of players n e.g. {2}
# Next n input lines -- Each player's rating


# Finds the minimum no. of candies to be distributed across players/team
def minCandieDist(score):
    
    candieCount = 0
    l = 0
    while l <= len(score)-1:  

        player1 = score[l]
        if l < len(score)-1:
            player2 = score[l+1]

        if l == 0 and player1 > player2:
            addnum = 2
            candieCount += addnum 
        elif l == 0 and player1 < player2:
            addnum = 1
            candieCount += addnum
        elif l == 0 and player1 == player2:
            addnum = 2 
            candieCount += addnum
        
        if l == len(score)-2 and player2 < player1 < prevplayer:
            addnum = 1
            candieCount += addnum
        else:
            if l > 0 and player1 < prevplayer:
                addnum = 1
                candieCount += addnum
            elif l > 0 and player1 > prevplayer:
                addnum += 1
                candieCount += addnum
            elif l > 0 and player1 == prevplayer:
                if addnum == 1:
                    candieCount += addnum
                else:
                    addnum -= 1
                    candieCount += addnum
        prevplayer = score[l]   #0-1, 1-2, 2-1, 3-2 4-1 5-2 6-3 7-4 8-
        l += 1
    return candieCount
 

# Queries user for number of players
def inputLen():
    teamnum = int(input().strip())
    return teamnum


# Queries user for player ratings
def inputParam(teamnum):
    score = []
    for l in range(teamnum):
        inputvar = int(input().strip())
        score.append(inputvar)
    return score


# Calls inputLen & inputParam functions and passes return values to inputCheck function
def inputInit():
    teamnum = inputLen()
    score = inputParam(teamnum)
    cbit = inputCheck(teamnum, score)
    while not cbit:
        teamnum = inputLen()
        score = inputParam(teamnum)
        cbit = inputCheck(teamnum, score)
    return score


# Checks validity of user input against constraints
def inputCheck(teamnum, score):
    cbit = 1
    if teamnum < 1 or teamnum > pow(10,5):
        cbit = 0
    elif len(score) != teamnum:
        cbit = 0
    elif cbit:
        for l in range(len(score)):
            if score[l] < 1 or score[l] > pow(10,5):
                cbit = 0
                break
    return cbit


##########################################################################################################
############# Main Code Block ############################################################################

listvar = inputInit()
print(minCandieDist(listvar))


# Extra Test values
#a = [1,2,2]
#b = [2,4,3,5,2,6,4,5]
#c = [2,4,2,6,1,7,8,9,2,1]