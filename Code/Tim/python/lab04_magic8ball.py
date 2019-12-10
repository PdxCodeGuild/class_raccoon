import random
repeat = "y"
while repeat == "y":
    input("\n\n\n\n\n¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸\n What is your question for the all-knowing eight ball? \n¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸\n\n>")

    answer = ["Decidedly maybe... maybe.", "Probably not.", "Probably", "Sometimes I don\'t like giving answers. Deal with it.", "Let\'s wait and see what happens.", "You do not want to know the answer.", "My mother, the All Knowing Cue Ball, said if I don\'t have anything nice to say, I shouldn\'t say anything at all..."]

    print("\n\n\n", random.choice(answer), "\n\n\n")

    repeat = input("¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸\n Do you have another question for the all-knowing eight ball?\n¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸\n\n(y/n)>")
    if repeat == "n":
        print("\n\n\n++++++++++++++++++++++++++++++++++++++++++++++++++++\nFine, the eight ball was done answering you anyway.\n++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n\n")
