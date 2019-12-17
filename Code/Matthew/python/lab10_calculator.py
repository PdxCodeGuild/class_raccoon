
secret_variable = 50

equation = input('What is the equation? ')
# print(exec(equation))

equation = equation.split(' ')

# equation = list(equation)
# print(equation)
operand1 = int(equation[0])
operator = equation[1]
operand2 = int(equation[2])
if operator == '+':
    print(f'{operand1} {operator} {operand2} = {operand1 + operand2}')

'hello world'.split(' ') # ['hello', 'world']
