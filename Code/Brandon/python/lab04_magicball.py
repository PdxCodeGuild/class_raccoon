#lab 04 Magic 8 ball, Brandon G.
import random

ball_response = ["It is certain","Of freaking course", "Not if your life depended on it","I cant answer that","Signs point to yes","Concentrate and ask again","My sources say no","Yes definitely","Reply hazy try again"]



while True:
    print("Welcome to magic 8 ball. Test your fate...")
    user_input = input("Go ahead, ask me a question...: ")
    answer = random.choice(ball_response)
    print(f"{user_input}..really? {answer}")

    if input('play again? ') == 'no':
        break
