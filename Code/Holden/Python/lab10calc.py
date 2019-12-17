import string
operators = ["+","-","/","*"]
excl=string.ascii_lowercase+string.whitespace
uop=""
start=0
looped=""
while True:
    start += 1
    if start == 2:
        looped =" (input exit to quit)"
    usin = input("Please input the equation you wish to perform (two variables only)"+looped+": ").lower()
    if usin == "quit" or usin == "exit":
        break
    usin = "".join(char for char in usin if char not in excl)
    for op in operators:
        splt=usin.find(op)
        if usin.find(op) != -1:
            if not usin[:splt].isdigit() and not usin[splt+1:].isdigit():
                print("Please input valid digits to equate.")
                break
            if op == "+":
                print(int(usin[:splt])+int(usin[splt+1:]))
                break
            elif op == "-":
                print(int(usin[:splt])-int(usin[splt+1:]))
                break
            elif op == "*":
                print(int(usin[:splt])*int(usin[splt+1:]))
                break
            elif op == "/":
                if int(usin[splt+1:]) == 0:
                    print("infinity")
                    break
                print(int(usin[:splt])/int(usin[splt+1:]))
                break
    if splt == -1:
        print("Please input a valid equation.")
        break
