#Magic 8 ball
import random
continue_yn = "yes"
#List of responses
answer_list = ["Absolutly not", "How should I know, I'm an 8 ball", "Probably", "You look weird from this angle", "Sure", "Let me ask my magic 8 ball", "Why would you even ask that?", "Does the pope shit in the woods?"]
print("I am the all seeing all knowing 8 ball (tm)! Ask a question and an answer ye shall receive!")
while continue_yn == "yes":
    input("What is your question for the mighty 8 ball? ")
    chosen_answer = random.choice(answer_list)
    print(f"\n {chosen_answer} \n")
    continue_yn = input("The magic sphere of black plastic has spoken, would you like to ask another question? ").lower()
else:
    print("Take your answers and leave then, mortal!")
