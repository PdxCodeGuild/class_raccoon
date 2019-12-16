

import random

target = random.randint(1,10)
print(target)
guesses = []
count = 0
while True:
    guess = int(input('Guess a number: '))
    if guess in guesses:
        print('you already guessed that, what\'s wrong with you?!?')
        continue

    if target == guess:
        print('Correct!')
        break
    elif target < guess:
        print('too high')
    else:
        print('too low')

    if len(guesses) > 0:
        last_guess = guesses[-1]
        # last_guess = guesses[len(guesses)-1]
        d_current = abs(target-guess)
        d_last = abs(target-last_guess)

        if d_current < d_last:
            print('closer')
        elif d_current > d_last:
            print('further')
        else:
            print('same distance')
    guesses.append(guess)

    count += 1
else:
    print('you lost!')
