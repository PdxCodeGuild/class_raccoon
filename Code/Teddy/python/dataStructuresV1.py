'''
Computer Science - Data Structures
Version 1 - Stack

Using the following Node class, let's implement some data structures.

class Node:
    def __init__(self, element, next=None):
        self.element = element
        self.next = next

    def __str__(self):
        return f'({self.element}, {self.next is not None})'

A stack can be visualized like a stack of plates, and provides two main methods:
push which adds an element to the top, and pop which removes an element from the top and returns it.
A stack is a FILO "first-in-last-out" data structure.

Stub:

class Stack:
  def __init__(self):
    self.root = None
  def push(self, element): # insert an element at the start
    ...
  def pop(self): # remove an element from the start
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

class Node:
    def __init__(self, element, next=None):
        self.element = element
        self.next = next

    def __str__(self):
        return f'({self.element}, {self.next is not None})'

class Stack:
    def __init__(self):
        self.root = None

    def push(self, element): # insert an element at the start
        self.root = Node(element, self.root)

    def pop(self): # remove an element from the start
        # pass
        if self.root is None:
            return None
        e = self.root.element
        self.root = self.root.next
        return e

    def peek(self): # returns the element on the root node or None
        return self.root.element

    def length(self): # return the number of elements
        count = 1
        last_node = self.root
        while last_node.next is not None:
            last_node = last_node.next
            count += 1
        return count

    def __str__(self):
        output = []
        node = self.root
        while node is not None:
            output.append(str(node.element))
            node = node.next
        return ','.join(output)

s = Stack()

s.push(5)
s.push(6)
s.push(6)
print(s)
print(s.pop()) # 6
print(s)

print(s.length())
