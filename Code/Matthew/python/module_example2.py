
import module_example1
print(module_example1.x)
print(module_example1.add(5, 2))

import module_example1 as m
print(m.x)
print(m.add(5, 2))

from module_example1 import x, add
print(x)
print(add(5, 2))


# x = 5
# def myfunc():
#     x = 10
#     print(x)
# myfunc()
# print(x)


from package1.module_example3 import y
print(y)


if __name__ == '__main__':
    print('user is running module 2, rather than importing')
