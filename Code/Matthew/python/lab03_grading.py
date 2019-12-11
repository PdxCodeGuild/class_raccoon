


def get_letter_grade(grade):
    if grade >= 100:
        return 'A+'

    ones_digit = grade % 10
    plus_minus = '+' if ones_digit > 5 else '-'

    plus_minus = ''
    if grade >= 100 or ones_digit > 5:
        plus_minus = '+'
    elif ones_digit < 5:
        plus_minus = '-'

    if grade >= 90:
        return 'A' + plus_minus
    elif grade >= 80:
        return 'B' + plus_minus
    elif grade >= 70:
        return 'C' + plus_minus
    elif grade >= 60:
        return 'D' + plus_minus
    else:
        return 'F'


while True:
    grade = input('What is your number grade? ')
    if grade.isdigit():
        grade = int(grade)
        break
    else:
        print('please enter a valid number')
    
    try:
        grade = int(grade)
        break
    except ValueError:
        print('please enter a valid number')

letter_grade = get_letter_grade(grade)
print(f'Your grade is {letter_grade}')



