'''
Lab 14: Credit Card Validation

Let's write a function which returns whether a string containing a credit card number is valid as a boolean. The steps are as follows:

Convert the input string into a list of ints
Slice off the last digit. That is the check digit.
Reverse the digits.
Double every other element in the reversed list.
Subtract nine from numbers over nine.
Sum all values.
Take the second digit of that sum.
If that matches the check digit, the whole card number is valid.
For example, the worked out steps would be:

4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5
4 5 5 6 7 3 7 5 8 6 8 9 9 8 5
5 8 9 9 8 6 8 5 7 3 7 6 5 5 4
10 8 18 9 16 6 16 5 14 3 14 6 10 5 8
1 8 9 9 7 6 7 5 5 3 5 6 1 5 8
85
5
Valid!
'''


#test variable turned into a list so that we can mess w each indicy of the list
card_num = list('4556737586899855')

# card_num = list(input("Credit Card Number: "))

for i in range(len(card_num)): # doing a for loop to turn each indicy into an integer
    card_num[i] = int(card_num[i])

#print(card_num)
check_digit = card_num.pop(-1) #took the last digit out of the list
#print(card_num)

card_num.reverse()#reversed order of numbers
#print(card_num)

for i in range(0, len(card_num), 2):# doubled every other int in the list
    card_num[i] = card_num[i]*2
#print(card_num)

for i in range(len(card_num)):# subtracted 9 from any indicy greater than 9
    if card_num[i] > 9:
        card_num[i] = card_num[i] - 9
#print(card_num)

total = str(sum(card_num)) #took the sum of the list. turned the list into a string
print(total)
print(check_digit)
if int(total[1]) == check_digit:#if the second digit of the sum = the check digit, its true. had to convert the string to an int.
    print("Valid")
