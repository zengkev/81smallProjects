'''DNA Visualization: animation of DNA'''

print('By Jing Wei Zeng')
print('Linkedin: https://www.linkedin.com/in/zengkev/')
print()
print()

import random, sys, time

Pause = .15

Rows = [
    #123456789
    '          ##',
    '         #{}-{}#',
    '        #{}---{}#',
    '       #{}-----{}#',
    '      #{}------{}#',
    '      #{}----{}#',
    '       #{}---{}#',
    '        #{}-{}#',
    '          ##',
    '        #{}-{}#',
    '       #{}---{}#',
    '      #{}-----{}#',
    '      #{}------{}#',
    '       #{}-----{}#',
    '       #{}-----{}#',
    '        #{}---{}#',
    '         #{}-{}#',]
    #123456789

try:
    print('DNA Animation')
    rowIndex = 0
    time.sleep(2)

    while True:
        # increment rowIndex to draw next row:
        rowIndex = rowIndex + 1
        if rowIndex == len(Rows):
            rowIndex = 0
        # Row index 0 and 9 don't have nucleotides:
        if rowIndex == 0 or rowIndex == 9:
            print(Rows[rowIndex])
            continue

        # Select random nucleotides pairs, 
        randomSelection = random.randint(1, 4)
        if randomSelection == 1:
            leftNucleotide, rightNucleotide = 'A', 'T'
        elif randomSelection == 2:
            leftNucleotide, rightNucleotide = 'T', 'A'
        elif randomSelection == 3:
            leftNucleotide, rightNucleotide = 'C', 'G'
        elif randomSelection == 4:
            leftNucleotide, rightNucleotide = 'G', 'C'
        
        # Print the new row
        print(Rows[rowIndex].format(leftNucleotide, rightNucleotide))
        time.sleep(Pause)
        

except KeyboardInterrupt:
    sys.exit()