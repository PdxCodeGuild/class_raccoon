class Node:
    def __init__(self, element, next=None):
        self.element = element
        self.next = next

    def __str__(self):
        return f"({self.element}, {self.next is not None})"

class Stack:
  def __init__(self):
    self.root = None
  def push(self, element): # insert an element at the start (new root)
    self.root = Node(element, self.root)
  def pop(self): # remove an element from the start (the root becomes the next node)
    prev_node = self.root
    self.root = self.root.next
    return prev_node.element
  def peek(self): # returns the element on the root node or None if there is no root
    return self.root.element
  def length(self): # return the number of elements
    count = 0
    node = self.root
    while node != None:
      node  = node.next
      count += 1
    return count
  def __str__(self):
    output = []
    node = self.root
    while node != None:
      output.append(node.element)
      node = node.next
    return str(output)



# s = Stack()
# s.push(5)
# s.push(6)
# print(s.length()) # 2
# print(s.pop()) # 6
# print(s.pop()) # 5



class LinkedList:
  def __init__(self):
    self.root = None
    self.first = None
  def append(self, element): # add the element to the end
    if self.root == None:
      self.root = Node(element, self.root)
      self.first = self.root
    else:
      self.root = Node(element, self.root)
  def insert(self, element, index): # insert the element at the given index
    
        
  def remove(self, element): # remove the first occurrence of the element
    pass
  def find(self, element): # find the first occurrence of the element and return it
    pass
  def length(self): # return the length of the list
    count = 0
    node = self.root
    while node != None:
      node  = node.next
      count += 1
    return count
  def __str__(self):
    output = []
    node = self.root
    while node != None:
      output.append(node.element)
      node = node.next
    return str(output)


nums = LinkedList()
nums.append(5)
nums.append(6)
nums.insert(7, 1)
print(nums) 
# print(nums.find(5)) # 1
# nums.remove(5)
# print(nums) # [7, 6]
# print(nums.length()) # 2