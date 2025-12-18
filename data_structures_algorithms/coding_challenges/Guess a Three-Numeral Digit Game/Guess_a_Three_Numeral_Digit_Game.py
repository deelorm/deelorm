
#Task -- Generates a secret 3-digit number & asks user to guess a number while awarding points if guess matches secret number

import random
NUM_SIZE = 3
MAX_GUESS = 10

#Matches user's guess with secret number & awards reward points
def main():
    print(''' 
    
    I have a Secret Number in mind.
    The secret number is made up of 3 distinct digits.
    Anyone is allowed to guess for a reward..................
    Also you are limited to {} attempts to make a right guess.

    As part of the game, you would be offered a hint/clue after each attempt as a response to 
    give you an idea of how close you were to the answer, if the response was not absolute.

    ###A HINT/CLUE### OF  ###MEANING####
         FEMTO            A digit from guess is matched at exact index of secret Number  
         PICO             A digit from guess is part of secret Number contained at a different index 
         NANO             Guess digits does not match secret Number

    '''.format(MAX_GUESS))
    print("##########################################################################################")
    print("")

    rewardPnts = 100
    while True:
        
        secretNum = secretNumber()    #Generates a secret 3-digit number

        print("I have a secret number")
        print("+++++++++++++++++++++++")
        print("")

        while guessNum <= MAX_GUESS:
            guessNum = 1
            guess = ""                 
            while len(guess) != NUM_SIZE or not guess.isdecimal():
                print("Guess #{}: ".format(guessNum))
                guess = input("> ")             #Takes user input guess

            clue = guessResp(guess, secretNum)   #Generates clue/hint in response to guess
            print(clue)
            guessNum += 1
       
            if guess == secretNum:
                print("You have been awarded {} points.".format(rewardPnts))
                break
            else:
                rewardPnts -= 10
            
        if guessNum > MAX_GUESS or guess == secretNum:
            print("")
            print("Do you want to play this game once more? yes or no")
            if not input("> ").lower().startswith("y"):
                break


#Generates a 3-digit random number
def secretNumber():
    number = list('0123456789')
    random.shuffle(number)  #Shuffles list of digits from 0-9
    correctNum = []

    for l in range(NUM_SIZE):
        correctNum += number[l]
    correctNum = "".join(correctNum)

    return correctNum


#Returns a list of responses based on the guess and secretNum; Femto, Pico & Nano
def guessResp(guess, secretNum):
    clue = []
    if guess == secretNum:   #If guess was absolutely right
        print("You guessed right...Kudos!!!")

    if True:
        for l in range(len(guess)):
            if guess[l] == secretNum[l]:
                clue.append('Femto')    #If guess-digit matches secret-number digit index-wise
            elif guess[l] in secretNum:
                clue.append('Pico')    #If guess-digit is contained as part of the secret-number

    if len(clue) == 0:
        clue.append("Nano")   #If guess-digit is different from secret-number

    clue.sort()     #Sorts clue responses to avoid user from having extra hint    
    clue = " ".join(clue)
    return clue


#################################################################################
################ Main Block of Code #############################################

main()