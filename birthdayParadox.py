"""Generate large amount of simulations on a set group of randomized birthdays, 
    show the probability of how much group contains group member with the same birthday"""

print('Linkedin: https://www.linkedin.com/in/zengkev/')


import datetime, random

def getBirthdays(numberofBirthdays):
    "return set of random birthdays"

    birthdays = []
    for i in range(numberofBirthdays):
        startOfYear = datetime.date(2001, 1, 1)
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays

def getMatch(birthdays):
    "Return the date object in set of birthdays that occurs more than once"
    if len(birthdays) == len(set(birthdays)):
        return None
    '''birthdays = ['Jan 1', 'Feb 2', 'Jan 1']
        len(birthdays) = 3
        set(birthdays) = {'Jan 1', 'Feb 2'} → only 2 elements
        Since 3 != 2, the condition is false and return None is not executed.'''
    
    # this can be faster probably by doing a binary search if set gets too big
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a+1 :]): # start at 2nd base
            if birthdayA == birthdayB:
                return birthdayA #return the matching birthday 
            
# Intro code

MONTHS = ('Jan', 'Feb', 'Mar', 'Apri', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:
    print('How many birthdays shall we generate? (MAX 100)')
    response = input('> ')
    if response.isdigit() and (0 < int(response) < 100):
        numBDays = int(response)
        break

print()


# Generate and display the birthdays

print("Here are", numBDays, 'birthdays')
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(', ', end='') # add , before all birthday but first

    monthName = MONTHS[birthday.month-1] #if birthday.month is 12 then position is 11
    dateText = '{}{}'.format(monthName, birthday.day)
    print(dateText, end='')

print()
print()

# Determine if there are two birthdays that match

match = getMatch(birthdays)
print("In this simulation: ", end='')
if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = '{}{}'.format(monthName, match.day)
    print('multiple people have birtday on: ', dateText)
else:
    print("No matching birthdays")
print()

simulationTime = int(input('How many simulations? '))
print('''Run this for {:,} times 
        with status report at 10,000'''.format(simulationTime))
print('Generate', numBDays, 'random birthdays 100,000 times')
input('Press Enter to begin....Warning!! this will take a long time')
print('Alrighty, you asked for it')

simCount = 0
for i in range(simulationTime):
    if i % 10_000 == 0:
        print(i, 'simulation run and ', simulationTime - i, 'to go')
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) != None:
        simCount = simCount + 1
print('{} simulation run completed.'.format(simulationTime))


# Display the probability and sim result:
probability = round(simCount / simulationTime * 100, 2)
print('Out of {} simulation of'.format(simulationTime), numBDays, 'people, there was a')
print('matching birthday in that group', simCount, 'times. This means')
print('that', numBDays, 'people have a', probability, '% chance of')
print('having a matching birthday in their group')


