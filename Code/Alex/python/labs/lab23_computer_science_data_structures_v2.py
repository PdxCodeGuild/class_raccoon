'''
Lab 23: Computer Science - Data Structures

Version 2 - Linked List

A linked list is like a regular list in Python, and provides methods for adding and removing elements.

Stub:

class LinkedList:
  def __init__(self):
    self.root = None
  def append(element): # add the element to the end
    ...
  def insert(element, index): # insert the element at the given index
    ...
  def remove(element): # remove the first occurrence of the element
    ...
  def find(element): # find the first occurrence of the element and return it
    ...
  def length(self): # return the length of the list
    ...

nums = LinkedList()
nums.append(5)
nums.append(6)
nums.insert(7, 0)
print(nums) # [7, 5, 6]
print(nums.find(5)) # 1
nums.remove(5)
print(nums) # [7, 6]
print(nums.length()) # 2
'''