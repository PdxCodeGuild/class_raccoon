#stacknode.py
class Node:
    def __init__(self, element, next=None):
        self.element = element
        self.next = next

class Stack:
    def __init__(self):
        self.root = None
    def push(self, element):
        if self.root == None:
            self.root = Node(element)
        else:
            self.root = Node(element, self.root)
    def pop(self):
        a = self.root.element
        self.root = self.root.next
        return a
    def peek(self):
        b = self.root.element
        return b
    def length(self):
        counter = 0
        x = self.root
        while x != None:
            counter += 1
            x = x.next
        return counter

s = Stack()
s.push(5)
s.push(6)
print(s.length())
print(s.pop())
print(s.pop())

# class LinkedList:
#   def __init__(self):
#     self.root = None
#   def append(element): # add the element to the end
#     if self.root == None:
#         self.root = element
#     else:
#         self.root = self.root + element
#   def insert(element, index): # insert the element at the given index
#     ...
#   def remove(element): # remove the first occurrence of the element
#     ...
#   def find(element): # find the first occurrence of the element and return it
#     ...
#   def length(self): # return the length of the list
#     ...
#
# nums = LinkedList()
# nums.append(5)
# nums.append(6)
# nums.insert(7, 0)
# print(nums) # [7, 5, 6]
# print(nums.find(5)) # 1
# nums.remove(5)
# print(nums) # [7, 6]
# print(nums.length()) # 2