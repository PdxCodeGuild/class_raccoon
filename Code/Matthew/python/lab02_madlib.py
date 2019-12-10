

continue_playing = 'yes'
while continue_playing == 'yes':

    adjective = input('Enter an adjective: ')
    verb_ending_ed = input('Enter a verb ending in \'ed\': ')
    nouns = input('Enter two plural nouns (separated by spaces): ')
    nouns = nouns.split(' ')
    noun_plural1 = nouns[0]
    noun_plural2 = nouns[1]
    print(nouns)
    liquid = input('Enter a liquid: ')
    famous_person = input('Enter a famous person: ')
    place = input('Enter a place: ')


    output = f'I enjoy long, {adjective} walks on the beach, getting {verb_ending_ed} in the rain and serendipitous encounters with {noun_plural1}. I really like piña coladas mixed with {liquid}, and romantic, candle-lit {noun_plural2}. I am well-read from Dr. Seuss to {famous_person}. I travel frequently, especially to {place}, when I am not busy with work.'

    print(output)
    
    continue_playing = input('Would you like to play again? yes/no: ')

# noun = input('Enter a noun: ')
# past_tense_verb = input('Enter a past-tense verb: ')
# output = f'Today I bought {noun} and it {past_tense_verb}'
# print(output)




