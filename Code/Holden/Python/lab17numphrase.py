first_digit=["","one","two","three","four","five","six","seven","eight","nine"]
second_digit=["","teen","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
while True:
    usin=input("Give me a number from 1-999: ")
    if usin.isdigit() and int(usin) < 1000:
        break
    if usin == exit:
        quit()
    print("Input invalid")
if usin == "404":
    print("ERROR 404 NOT FOUND")
places = []
for i in usin:
    places.append(int(i))
places.reverse()
if len(places)==3:
    print(first_digit[places[2]]+" hundred", end=" ")
if len(places) > 1:
    if places[1] == 1:
        if places[0] == 0:
            print("ten")
        elif places[0] == 1:
            print("eleven")
        elif places[0] == 2:
            print("twelve")
        elif places[0] == 3:
            print("thirteen")
        elif places[0] == 5:
            print("fifteen")
        else:
            print(first_digit[places[0]]+"teen")
    else:
        print(second_digit[places[1]]+" "+first_digit[places[0]])

else:
    print(first_digit[places[0]])
