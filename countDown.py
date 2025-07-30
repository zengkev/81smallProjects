'''Countdown: Showing a countdown in a display'''

print('Countdown by Jing Wei Zeng')
print('Linkedin: https://www.linkedin.com/in/zengkev/')
print()
print()

import sys, time, math
import sevseg # requires sevseg.py in same file

while True: 
    print("Enter your timer in seconds: ")
    secondsLeft = input("> ")
    if secondsLeft.isdecimal():
        secondsLeft = int(secondsLeft)
        break
    
    print("Enter your timer in seconds, like 50: ")
    continue    


try:
    while True:
        print('\n' * 60)
        hours = str(secondsLeft // 3600)
        minutes = str((secondsLeft % 3600) // 60)
        seconds = str(secondsLeft % 60)

        # Get the digit strings from the sevseg module:
        hDigits = sevseg.getSevSegStr(hours, 2)
        hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()

        mDigits = sevseg.getSevSegStr(minutes, 2)
        mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()

        sDigits = sevseg.getSevSegStr(seconds, 2)
        sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()

        # Display the digits
        print(hTopRow    + '       ' + mTopRow    + '       ' + sTopRow)
        print(hMiddleRow + '   *   ' + mMiddleRow + '   *   ' + sMiddleRow)
        print(hBottomRow + '   *   ' + mBottomRow + '   *   ' + sBottomRow)

        if secondsLeft == 0: 
            print()
            print('   * * * * BOOM * * * *')
            break

        print()
        print('Press CTRL + C to exit')
        
        time.sleep(1)
        secondsLeft -= 1

except KeyboardInterrupt:
    print('Countdown, Stopped by Jing Wei Zeng')
    sys.exit()

