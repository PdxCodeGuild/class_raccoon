import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self, p): # method, or 'member function'
        dx = self.x - p.x
        dy = self.y - p.y
        return math.sqrt(dx*dx + dy*dy)

    def scale(self, v):
        self.x *= v
        self.y *= v

    def __str__(self):
        return f'({self.x},{self.y})'


# p3 = Point()
# print(p3.x)
# print(p3.y)

p1 = Point(5,2)
p2 = Point(8,4)
p2.scale(2)
print(p1)
print(p2)
s = str(p1)
print(s)

dist = p1.distance(p2) # or p2.distance(p1), either works
print(dist)


# # similar to how we can call methods of the str class
# s = 'hello world'
# print(s.split(' '))


# import random
# print(random.randint(0,1))
#
# import datetime
# datetime.datetime.strptime(...)

