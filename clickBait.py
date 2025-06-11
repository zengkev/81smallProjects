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

def generateWhatYouDontKnowHeadline():
    noun = random.choice(NOUNS)
    pluralNoun = random.choice(NOUNS) + 's'
    when = random.choice(WHEN)
    return 'Without This {}, {} Could KILL You {}'.format(noun, pluralNoun, when)

def generateBigCompaniesHateHerHeadline():
    pronoun = random.choices(ojbectPronouns)
    state = random.choice(STATES)
    noun1 = random.choice(NOUNS)
    noun2 = random.choice(NOUNS)
    return 'Big Companies Hate {}!! See How This {} {} Invented a Cheaper {}'.format(pronoun, state, noun1, noun2)

def generateYouWontBelieveHeadline():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)
    pronoun = random.choice(possesivePronouns)
    place = random.choice(PLACES)
    return 'You won\'t Believe What This {} {} Found in {} {}'.format(state, noun, pronoun, place)


def generateDontWantYouToKnowHeadline():
    pluralNoun1 = random.choice(NOUNS) + 's'
    pluralNoun2 = random.choice(NOUNS) + 's'
    return 'What {} Don\'t Want You to Know About {}'.format(pluralNoun1, pluralNoun2)

def generateGiftIdeaHeadline():
    number = random.randint(7, 15)
    noun = random.choice(NOUNS)
    state = random.choice(STATES)
    return '{} Gift Ideas to Give Your {} From {}'.format(number, noun, state)

def generateReasonsWhyHeadline():
    number1 = random.randint(3, 19)
    pluralNoun = random.choice(NOUNS) + 's'
    number2 = random.randint(1, number1)
    return '{} Reasons Why {} Are More Interesting Than YOu Think (Number {} Will Surprise You@!!)'.format(number1, pluralNoun, number2)

def generateJobAutomatedHeadline():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)

    i = random.randint(0, 2)
    pronoun1 = possesivePronouns[i]
    pronoun2 = personalPronouns[i]
    if pronoun1 == 'Their':
        return 'This {} {} Didn\'t Think Robots Would Take {} Job.' \
        '{} Were Wrong.'.format(state, noun, pronoun1, pronoun2)
    else:
        return 'This {} {} Didn\'t Think Robots Would Take {} Job.' \
        '{} Was Wrong.'.format(state, noun, pronoun1, pronoun2)

if __name__=='__main__':
    main()

