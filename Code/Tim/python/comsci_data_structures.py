class Node:
    def __init__(self, element, next=None):
        self.element = element
        self.next = next
        self.root = None

    def push(self, element):
        ...

class Stack:
  def __init__(self):
    self.root = []

 # insert an element at the end
  def push(self, element):
    self.root.append(element)
    return self.root

  # def pop(self, element): # remove an element from the start
  def pop(self):
     return self.root.pop(-1)

# returns the element on the root node or None
  def peek(self):
    print(self.root[-1])

# return the number of elements
  def length(self):
    if len(self.root) != []:
        return None
    else:
        return len(self.root)

# # creates a string for returning
#   def __str__(self):
#       return str(self.root)

s = Stack()
s.push(5)
s.push(6)
s.push(9)
s.push(27)
s.push(2)
s.pop()
s.pop()
s.peek()
print(s)
# print(s.length()) # 2
# print(s.pop()) # 6
# print(s.pop()) # 5
