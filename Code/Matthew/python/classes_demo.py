

# this_is_snake_case
# thisIsCamelCase
# ThisIsPascalCaseOrTitleCase


class BigInt:
    def __init__(self, num_str):
        if isinstance(num_str, str):
            self.__num = [int(x) for x in reversed(num_str)]
        else:
            self.__num = num_str.copy()

    def __add__(self, b):

        # make copies so we don't change the original (side effect)
        num1 = self.__num.copy()
        num2 = b.__num.copy()

        # make sure both lists have the same length
        if len(num1) > len(num2):
            for i in range(len(num1)-len(num2)):
                num2.append(0)
        elif len(num1) < len(num2):
            for i in range(len(num2)-len(num1)):
                num1.append(0)

        # do the math
        carry = 0
        output = []
        for i in range(len(num1)):
            current_digit = carry + num1[i] + num2[i]
            carry = current_digit // 10
            output.append(current_digit % 10)
        if carry > 0:
            output.append(carry)
        return BigInt(output)

    def __str__(self):
        return ''.join([str(x) for x in self.__num[::-1]])

    def __repr__(self):
        return ''.join([str(x) for x in self.__num[::-1]])



# nums = ['567', '235', '54', '7']
# nums = [BigInt(num) for num in nums]
# print(nums)



a = BigInt('923')
b = BigInt('959')
# b = BigInt([9, 5, 9])
print(a)
print(b)
c = a + b
print(c)

# print(type(a))
# print(a)
# print(a.num)






# a = BigInt('5')
# b = BigInt('6')
# c = a.add(b)
# print(c) # 11