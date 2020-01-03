num1 = int(input("What is the first number? "))
num2 = int(input("What is the second number? "))

def recursive_multiplication(num1,num2):
    if num2 == 1:
        return num1
    
    total = num1 + recursive_multiplication(num1,(num2-1))
    return total

print(recursive_multiplication(num1,num2))