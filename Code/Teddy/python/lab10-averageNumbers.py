# Lab 10: Average Numbers

# average function
def Average(num):
    total_sum = 0
    for n in range(num):
        numbers = float(input('Input number : '))
        total_sum += numbers
    avg = total_sum/num
    return avg


numbers = int(input('How many numbers: '))


print(f'Average of {numbers} numbers is :{Average(numbers)}')
