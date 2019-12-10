#Mad Libs

continue_yn = "yes"
print("Hi, welcome to Lad Mibs mad libs! Please fill in the following blanks. /n")
while continue_yn == "yes":
    input1 = input("Please choose an object... ")
    input2 = input("Now an animal... ")
    input3 = input("Now a noun... ")
    input4 = input("Weird, looks like all I chose were nouns, add one that would be funny in front of the word 'balls'...")
    input5 = input("Yup, another noun...")
    print(f"How many {input1} must a {input2} walk down, before you call him a {input2}? How many {input3} must a white dove sail, before she sleeps in the sand? How many times must the {input4} balls fly before they're forever banned? The answer, my friend, is blowin' in the {input5} The answer is blowin' in the {input5}")
    continue_yn = input("Would you like to go again? (Yes, No) ").lower()
else:
    print("Thanks for playing!")
