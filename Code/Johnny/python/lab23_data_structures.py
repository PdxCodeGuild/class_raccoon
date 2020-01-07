class Node:
  def __init__(self, element, next):
    self.element = element
    self.next = next

    def __str__(self):
        return f'({self.element}, {self.next is not None})'


class Stack:
  def __init__(self):
    self.root = None

  def push(self, element): # insert an element at the start
    self.root = Node(element, self.root)

  def pop(self, element): # remove an element from the start
    if self.root is None:
        return None
    first_node = self.root
    self.root = self.root.next
    return first_node.element

  def peek(self): # returns the element on the root node or None
    if self.root is None:
        return None
    return self.root.element

  def length(self): # return the number of elements
    counter = 0
    node = self.root
    while node != None:
        node = node.next
        counter += 1
    return counter

  def __str__(self):
    output = []
    node = self.root
    while node != None:
        output.append(node.element)
        node = node.next
    return str(output)

start = Stack()
start.push(5)
start.push(6)
start.push(7)
start.push(8)
start.peek()
print(start.length()) # 2
# start.pop(6) # 6
# start.pop(8) # 8


print(start)
