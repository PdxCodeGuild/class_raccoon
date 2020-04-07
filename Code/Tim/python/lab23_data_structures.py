class Node:
  def __init__(self, element, next):
    self.element = element
    self.next = next

    def __str__(self):
        return f'({self.element}, {self.next is not None})'


class Hat:
  def __init__(self):
    self.root = None

  def push(self, element): # insert an element at the start
    self.root = Node(element, self.root)

  def pop(self): # remove an element from the start
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

hatstack = Hat()
hatstack.push('bowler')
hatstack.push('cap')
hatstack.push('beenie')
hatstack.push('tophat')
hatstack.pop()
hatstack.pop()
print(hatstack.peek())
print(hatstack)
