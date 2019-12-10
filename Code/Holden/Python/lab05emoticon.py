import random
print("welcome to the emoji generator")
eye = [":",";","X","B"]
brow = [">","|","/","]",""]
nose = ["-",""]
mouth = [")","(","[","]","3","o","O","c","C","D","p","U"]
cont = "y"
while cont != "no":
    browf=random.choice(brow)
    eyef=random.choice(eye)
    nosef=random.choice(nose)
    mouthf=random.choice(mouth)
    print(f"{browf}{eyef}{nosef}{mouthf}")
    cont = input("generate another?(No to quit)").lower()
