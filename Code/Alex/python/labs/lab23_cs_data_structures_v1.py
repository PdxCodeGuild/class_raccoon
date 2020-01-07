'''
Lab 23: Computer Science - Data Structures

Using the following Node class, let's implement some data structures.

class Node:
  def __init__(element, next=None):
    self.element = element
    self.next = next


Version 1 - Stack

A stack can be visualized like a stack of plates, and provides two main methods: push which adds an element to the top, and pop which removes an element from the top and returns it. A stack is a FILO "first-in-last-out" data structure.

Stub:

class Stack:
  def __init__(self):
    self.root = None
  def push(self, element): # insert an element at the start
    ...
  def pop(self, element): # remove an element from the start
    ...
  def peek(self): # returns the element on the root node or None
    ...
  def length(self): # return the number of elements
    ...
  def __str__(self):
    ...

s = Stack()
s.push(5)
s.push(6)
print(s.length()) # 2
print(s.pop()) # 6
print(s.pop()) # 5
'''
