'''Making a Month Calender'''

print('Caesar Cipher Hacker by Jing Wei Zeng')
print('Linkedin: https://www.linkedin.com/in/zengkev/')
print()
print()

import datetime
import calendar

DAYS = " ".join(calendar.day_name[-1:] + calendar.day_name[0:6]).split()
MONTHS = " ".join(calendar.month_name[0:]).strip().split()

# loop to get year from user
while True: 
    print("Enter the year: ")
    yearEntered = input("> ")
    year = int(yearEntered)
    if yearEntered.isdecimal() and year > 0 and len(yearEntered) == 4:
        break
    
    print("Enter a calender year, like 2025: ")
    continue

# loop to get month from user
while True:
    print("Enter a month (1-12): ")
    monthEntered = input("> ")
    if not monthEntered.isdecimal():
        print("Enter a numeric month, like 5 for May.")
        continue

    month = int(monthEntered)
    if 1 <= month <= 12:
        break

    print("Please enter a number from 1 to 12.")


def getCalendar(year, month):
    calText = ''

    calText += (' ' * 34) + MONTHS[month - 1] + ' ' + str(year) + '\n'
    for day in DAYS:
        calText += '...' + day
    calText += '..\n'

    weekSeparator = ('+----------' * 7) + '+\n'
    blankRow = ('|          ' * 7) + '+\n'

    currentDate = datetime.date(year, month, 1)
    while currentDate.weekday() != 6:
        currentDate -= datetime.timedelta(days = 1)
    
    while True:
        calText += weekSeparator

        dayNumberRow = ''
        for i in range(7):
            dayNumberLabel = str(currentDate.day).rjust(2)
            dayNumberRow += '|' + dayNumberLabel + (' ' * 8)
            currentDate += datetime.timedelta(days=1)
        dayNumberRow += '|\n'

        calText += dayNumberRow
        for i in range(3):
            calText += blankRow
        
        if currentDate.month != month:
            break
    calText += weekSeparator
    return calText

calText = getCalendar(year, month)
print(calText)


# Draw the graph line vertical and horizontal

# Roll out the calendar

