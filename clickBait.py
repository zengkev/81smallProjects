'''Clickbait Generator for Headline'''

print('Clickbait Headline Generator by Jing Wei Zeng')
print('Linkedin: https://www.linkedin.com/in/zengkev/')
print()
print()

import random

# let's set up some basice wordlist

ojbectPronouns = ['Her', 'Him', 'Them']
possesivePronouns = ['Her', 'Him', 'Their']
personalPronouns = ['She', 'He', 'They']
STATES = ["Alaska", "Alabama", "Arkansas", "American Samoa", 
          "Arizona", "California", "Colorado", "Connecticut", 
          "District ", "of Columbia", "Delaware", "Florida", 
          "Georgia", "Guam", "Hawaii", "Iowa", "Idaho", 
          "Illinois", "Indiana", "Kansas", "Kentucky", 
          "Louisiana", "Massachusetts", "Maryland", "Maine", 
          "Michigan", "Minnesota", "Missouri", "Mississippi", 
          "Montana", "North Carolina", "North Dakota", 
          "Nebraska", "New Hampshire", "New Jersey", 
          "New Mexico", "Nevada", "New York", "Ohio", 
          "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", 
          "Rhode Island", "South Carolina", "South Dakota", 
          "Tennessee", "Texas", "Utah", "Virginia", 
          "Virgin Islands", "Vermont", "Washington", 
          "Wisconsin", "West Virginia", "Wyoming"]
NOUNS = ['Athlete', 'Clown', 'Shovel', 'Paleo Diet', 'Doctor',
          'Parent', 'Cat', 'Dog', 'Chicken', 'Robot', 'Video Game',
          'Avocado', 'Plastic Straw', 'Serial Killer', 
          'Telephone Psychic']
PLACES = ['House', 'Attic', 'Bank Deposit Box', 'School',
          'Basement', 'Workplace', 'Donut Shop', 'Apocalypse Bunker']
WHEN = ['Soon', 'This Year', 'Later Today', 'RIGHT NOW', 'Next Week']



def main():
    print('Clickbait headline generator')
    print('By Jing Wei Zeng')
    print()

print('Our website needs to trick people into clicking ads')
while True:
    print('Enter the number of clickbait headlines to generator:')
    response = input('> ')
    if not response.isdecimal():
        print('Please enter a number')
    else:
        numberOfHeadlines = int(response)
        break

for i in range(numberOfHeadlines):
    clickBaitType = random.randint(1, 8)

    if clickBaitType == 1:
        headline = generateAreMillennialsKillingHeadline()
    elif clickBaitType == 2:
        headline = generateWhatYouDontKnowHeadline()
    elif clickBaitType == 3:
        headline = generateBigCompaniesHateHerHeadline()
    elif clickBaitType == 4:
        headline = generateYouWontBelieveHeadline()
    elif clickBaitType == 5:
        headline = generateDontWantYouToKnowHeadline()
    elif clickBaitType == 6:
        headline = generateGiftIdeaHeadline()
    elif clickBaitType == 7:
        headline = generateReasonsWhyHeadline()
    elif clickBaitType == 8:
        headline = generateJobAutomatedHeadline()
    
    print(headline)
print()

website = random.choice(['wobsite', 'blag', 'FaceBuuk', 'Googles', 
                         'Facesbook', 'Tweedie', 'Pastagram'])
when = random.choice(WHEN).lower()
print('Post these to our', website, when, 'or you\'re fired')

def generateAreMillennialsKillingHeadline():
    noun = random.choice(NOUNS)
    return 'Are Millennials Killing the {} Industry?'.format(noun)

    noun = random.choice(NOUNS)
    pluralNoun = random.choice(NOUNS) + 's'
    when = 


if __name__=='__main__':
    main()

