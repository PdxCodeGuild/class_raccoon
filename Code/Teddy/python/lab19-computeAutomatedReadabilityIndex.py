'''
Lab 19: Compute Automated Readability Index
Compute the ARI for a given body of text loaded in from a file. The automated readability index (ARI) is a formula
for computing the U.S. grade level for a given block of text. The general formula to compute the ARI is as follows:

ARI Formula

ARI = 4.71(characters/words) + 0.5(words/sentences) - 21.43

The score is computed by multiplying the number of characters divided by the number of words by 4.71,
adding the number of words divided by the number of sentences multiplied by 0.5, and subtracting 21.43.
If the result is a decimal, always round up.
Scores greater than 14 should be presented as having the same age and grade level as scores of 14.

Scores correspond to the following ages and grade levels:

    Score  Ages     Grade Level
     1       5-6    Kindergarten
     2       6-7    First Grade
     3       7-8    Second Grade
     4       8-9    Third Grade
     5      9-10    Fourth Grade
     6     10-11    Fifth Grade
     7     11-12    Sixth Grade
     8     12-13    Seventh Grade
     9     13-14    Eighth Grade
    10     14-15    Ninth Grade
    11     15-16    Tenth Grade
    12     16-17    Eleventh grade
    13     17-18    Twelfth grade
    14     18-22    College
Once you’ve computed the ARI score, you can use the following dictionary to look up the age range and grade level.

ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}
The output should look something like the following:

--------------------------------------------------------

The ARI for gettysburg-address.txt is 12
This corresponds to a 11th Grade level of difficulty
that is suitable for an average person 16-17 years old.

--------------------------------------------------------
'''

#  Import libraries
import requests
import re
import string
import math

# ARI scale dictionary
ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

# Import file
response = requests.get('http://www.gutenberg.org/cache/epub/60939/pg60939.txt')
text = response.text
# Translate to lowercase
text = text.lower()

# Get number of Characters function
def charactersCount(text):
    # remove all the punctuations
    for punctuation in string.punctuation:
        # replaced by space
        text = text.replace(punctuation, ' ')
    # find all characters in text by using expression
    text = re.findall(r'\w', text)

    # Count all Characters by starting from 0
    count = 0
    for char in text:
        count  += 1
    # Return value
    return count

# Get number of Words function
def wordsCount(text):
    # find all Words in text by using expression
    text = re.findall(r"\w+'*\w+", text)

    # Count all Words by starting from 0
    count = 0
    for word in text:
        count  += 1
    # Return value
    return count

# Get number of Sentence function
def sentencesCount(text):
    # find all sentences in text by using expression
    text = re.split(r'[.?!]', text)

    # Count all Sentences by starting from 0
    count = 0
    for sent in text:
        count  += 1
    # Return value
    return count

# Counting ARI function
def ariNumber(char, word, sent):
    # ARI formula and round up
    ari_number = math.ceil(4.71*(char/word) + 0.5*(word/sent)- 21.43)
    # Return value
    return ari_number

def matchDict(ariNumber):
    if ari_number in ari_scale:
        return ari_scale[ariNumber]

char = charactersCount(text)

word = wordsCount(text)

sent = sentencesCount(text)

ari_number = ariNumber(char, word, sent)
# print(ari_number)
grade_level = matchDict(ari_number)['grade_level']

age_level = matchDict(ari_number)['ages']

# Output
print('***********************************')
print()
print(f'The ARI for The Project Gutenberg EBook of Superjoemulloy, by Scott F. Grenville is {ari_number}')
print(f'This corresponds to a {grade_level} level of difficulty')
print(f'that is suitable for an average person {age_level} years old.')
print()
print('***********************************')
