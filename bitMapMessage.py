''' This program uses a multiline string to draw a 2D image of a map
    using bitmap.splitlines() and message[i % len(message)]'''

<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD

print('Linkedin: https://www.linkedin.com/in/zengkev/')


=======
>>>>>>> b6747c44b6259022f16813e27d0f95f5da950ee8
=======
>>>>>>> 1e298c03066de36845fbaec13b4c5f0cee648c75
>>>>>>> dev
import sys


bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
...................................................................."""


print('Bitmap by Jing Wei Zeng')
print('Enter the message you want to display on the bitmap.')

message = input('Example like: Hello! or your take: ')
if message == '':
    sys.exit()

# let's loop over each line of bitmap with the your message

for line in bitmap.splitlines():
    # loop over each charater in each line
    for i, bit in enumerate(line):
        if bit == ' ':
            print(' ', end='')
        else:
            print(message[i % len(message)], end='')
    print()
    