
import datetime
import random


#Returns a list of dates for a given number of birthdays/people
def getBirthdays(numBDays):

    birthdays = []
    for l in range(numBDays):
        if l > 30:
            day = random.randint(1,30)
        elif l == 0:
            day = l + 1
        else:
            day = l

        startDay = datetime.date(2022, 1, day) #Generates random dates between 1-1-2022
        randomDay = datetime.timedelta(random.randint(1,365)) #Returns a day in a year calendar
        birthdays.append((startDay + randomDay).strftime('%b %m'))

    return birthdays


#Returns a date that is common to two or more people
def getMatch(birthdays):
    bdays = []
    if len(birthdays) == len(set(birthdays)):    #If there are no duplicate dates
        return None
    elif True:
        for a,birthdayA in enumerate(birthdays):
            for b,birthdayB in enumerate(birthdays[a+1:]):
                if birthdayA == birthdayB:            #If a date appears more than once
                    bdays.append(birthdayA)
    return bdays

#Returns a unique set of dates
def unqDates(matchDay):
    l = 0
    while l <= len(matchDay)-1:
        n = l + 1
        while n <= len(matchDay)-1:
            if matchDay[l] == matchDay[n]:
                del matchDay[n]
                n -= 1
            n += 1
        l += 1
    return matchDay


#Gives an overview of the chances of having common dates among a group of people
def main():
    print('''
    This situational, analytical program determines the chances of the same date for a list of 
    different dates, which are birthdays for different people, re-occuring multiple times for 
    a given number of people.
    
    It goes on to provide an overview of how probable two or more people would luckily share
    the same birthday. Also it only accepts a number between 1 & 100 inclusive for it to provide
    further breakdown info.
    ''') 
    print("+---------------------------------------------------------------------------------------------------+")
    
    while True:
        print('..............................Program Inception...............................')
        numBDays = 0
        print("")
        print("How many birthdays do you want me to generate (max.100)? ")

        while (not str(numBDays).isdecimal()) or (numBDays < 1 or numBDays > 100): #Takes user input & checks if it is decimal
            numBDays = int(input("> "))                                  #and whether it falls within constraint
                                                                        
        print("The list of birthdays for {} people are: ".format(numBDays))
        birthdays = getBirthdays(numBDays)
    
        for a, birthdayA in enumerate(birthdays):  #Prints all dates for a given number of people
            print(birthdayA , end='')  
            if a != len(birthdays)-1:
                print(', ', end='')
        print("")
        print("")
        matchDay = getMatch(birthdays)     #Checks for common dates 
        matchDayUnq = unqDates(matchDay)
        if matchDay != None:
            print("There is a chance multiple people share {} date(s) as their birthday: ".format(len(matchDayUnq)), end='')
            
            for l in range(len(matchDayUnq)):
                print(matchDayUnq[l], end='')
                if l != len(matchDay)-1:
                    print(', ', end='')
            print('')
        else:
            print("There are seems to be no common dates for the given number of people.")
        print("")

        print('We perform an additional 100000 random simulations for {} people to check further for common dates..'.format(numBDays))
        print('')
        print('Start of simulation...')


        simDMatch = 0
        for l in range (100000):          #Performs an additional 100000 run
            if l % 10000 == 0:
                print(l, 'simulation run.' )    #Reports every 10000 simulation run
            birthdays = getBirthdays(numBDays)
            matchDaySim = getMatch(birthdays)

            if matchDaySim != None:
                for l in range(len(matchDaySim)):
                    if matchDaySim[l] in matchDayUnq:
                        simDMatch += 1                  #Increases count for every common date
                        break

        print("Simulation for 100000 runs completed.")


        probDMatch = round((simDMatch/100000 * 100), 2)
        print('''
    Out of an extra 100000 simulation runs for {} people or dates, there was/were {}
    common date(s) for the total simulations conducted. With the chances of having {}
    percent of the group having common dates/birthdays for the total number of people
    in the group.
        '''.format(numBDays, simDMatch, probDMatch))

        print("")
        print("Do you have an additional number representing different set of people to provide? yes or no")

        if not input("> ").lower().startswith('y'):
            break


############################################################################################################
############################################################################################################
############################## Main Block ##################################################################
############################################################################################################
############################################################################################################
        
main()


