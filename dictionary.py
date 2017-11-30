import json
from difflib import get_close_matches

# import the data
data = json.load(open('data.json'))

# function that searches the dictionary according to user input and returns appropriate response
def find_def(word):
    word = word.strip().lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif word == 'please quit':
        return 'You have quit.'
    elif len(get_close_matches(word, data.keys())) > 0:
        inp = input('Did you mean {} instead? Enter "y" or "n": '.format(get_close_matches(word, data.keys())[0])).strip().lower()
        if inp[:1] == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif inp[:1] == 'n':
            return '{} is not in this dictionary. Please try another word.'.format(word.capitalize())
        else:
            return 'We did not understand your entry.'
    else:
        return '{} is not in this dictionary. Try again.'.format(word.capitalize())

# create empty string for while loop
choice = ''

# while loop that allows user to search until they want to quit
while choice != 'please quit':

    choice = input('Enter a word to search, or type "please quit" to quit: ')
    output = find_def(choice)

    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)
