
import random


def number_to_phrase(num):
    ones_teens = ['zero','one','two','three','four','five','six','seven','eight','nine', 'ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    tens = ['zeroty','onety','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
    if num < 0:
        return 'no support for negative numbers'
    elif num < 20:
        return ones_teens[num]
    elif num < 100:
        ones_digit = num%10
        tens_digit = num//10
        if ones_digit == 0:
            return tens[tens_digit]
        else:
            return tens[tens_digit] + '-'  + ones_teens[ones_digit]
    elif num < 1000:
        ones_digit = num%10
        tens_digit = num//10%10
        hundreds_digit = num//100
        if tens_digit == 0:
            if ones_digit == 0:
                return ones_teens[hundreds_digit] + ' hundred'
            return ones_teens[hundreds_digit] + ' hundred ' + ones_teens[ones_digit]
        elif tens_digit == 1:
            return ones_teens[hundreds_digit] + ' hundred ' + ones_teens[num%100]
        elif ones_digit == 0:
            return ones_teens[hundreds_digit] + ' hundred ' + tens[tens_digit]
        return ones_teens[hundreds_digit] + ' hundred ' + tens[tens_digit] + '-' + ones_teens[ones_digit]


# num = int(input('Enter a number: '))
# print(number_to_phrase(num))

for i in range(1000):
    # num = random.randint(0,99)
    print(i, number_to_phrase(i))

