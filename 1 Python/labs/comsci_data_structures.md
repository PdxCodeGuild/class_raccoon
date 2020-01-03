


# Computer Science - Data Structures

Using the following Node class, let's implement some data structures.

```python
class Node:
  def __init__(element, next=None):
    self.element = element
    self.next = next
```

## Version 1 - Stack

A [stack](https://en.wikipedia.org/wiki/Stack_(abstract_data_type)) can be visualized like a stack of plates, and provides two main methods: `push` which adds an element to the top, and `pop` which removes an element from the top and returns it. A stack is a `FILO` "first-in-last-out" data structure.


Stub:
```python
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
```



## Version 2 - Linked List

A [linked list](https://en.wikipedia.org/wiki/Linked_list) is like a regular list in Python, and provides methods for adding and removing elements.

Stub:
```python
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
```








