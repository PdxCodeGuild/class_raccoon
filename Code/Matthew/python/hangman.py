import random

dictionary_path = r'../../../1 Python/data/english.txt'

#import text file
with open(dictionary_path, "r") as file:
    wordlist = file.read().split("\n")

#filter words <= 5 letters
wordlist = [word for word in wordlist if len(word) > 5]

#randomly choose word
compchoice = random.choice(wordlist)
# print(compchoice)

#split word into list of letters
compchoice = list(compchoice)
# print(compchoice)

#create blank list of guesses (underscores list)
guesslist = ["_" for letter in compchoice]
# print(guesslist)

#count guesses remaining

#make list of letters already guessed
alreadyguess = []

#create variable for user to input guesses
def runit():
    countrem = 10
    while countrem > 0:
        print(" ".join(guesslist))
        userguess = input("Guess a letter: ").casefold()
        if len(userguess) > 1 or not userguess.isalpha():
            print("Invalid entry!")
            continue
        if userguess in alreadyguess:
            print("You've already guessed that, dummy!")
            print(f"Current guesses: {' '.join(alreadyguess)}")
            continue
        alreadyguess.append(userguess)
        letter = userguess
        if letter in compchoice:
            for i in range(len(compchoice)):
                if compchoice[i] == letter:
                    guesslist[i] = letter
            print("Correct!")
        else:
            print("You have chosen poorly!")
            countrem -= 1
            print(f"You have {countrem} guesses left.")
        print()
        if "_" not in guesslist:
            print(''.join(compchoice))
            print("Good job, you won! OMGWTFBBQ")
            break
    if countrem == 0:
        print("Game over! The man is hunged!")    
        print(f"The word was {''.join(compchoice)}")
            
runit()        

#win/lose test