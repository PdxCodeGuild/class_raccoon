'''
Lab 23: Computer Science - Data Structures
'''

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
    node1 = self.root
    self.root = self.root.next
    return node1.element

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



s = Stack()
s.push(5)
s.push(6)
s.peek()
print(s.length())
print(s)



class LinkedList:

  def __init__(self):
    self.root = None

    def push(self, element): # add an element to the start
        self.root = Node (element, self.root)

  def append(self, element): # add the element to the end
    if self.root is None:
        print('setting root node')
        self.root = Node(element, None)
    else:
        current_node = self.root
        print('finding last node')
        while current_node.next is not None:
            print('current node ' + str(current_node.element))
            current_node = current_node.next
        print('last node is ' + str(current_node.element))
        current_node.next = Node(element)

  def insert(self, element, index): # insert the element at the given index
    if index == 0:
      self.push(element)
      return
    current_node = self.root
    counter = 0
    while current_node is not None:
        if counter == index-1:
            # create a new node containing the elements
            # set the next node of the new node equal to the next node of the current Node
            new_node = Node(element, current_node.next)
            # set the next node of the current node equal to the new node
            current_node.next = new_node
            break
        counter += 1
        current_node = current_node.next
    else:
        self.append(element)

  def remove(self, element): # remove the first occurrence of the element
    # if the list has no elements, just leave
    if self.root is None:
        return
    # If the first node is the one we want to remove
    # update self.root and leave
    if self.root is not None and self.root.element == element:
        self.root = self.root.next
        return
    # otherwise find the node which contains the element we're removing
    # maintain a reference to the current and previous node
    current_node = self.root
    previous_node = None
    while current_node is not None:
        if current_node.element == element:
            previous_node.next = current_node.next
            break
        previous_node = current_node
        current_node = current_node.next

  def find(self, element): # find the first occurrence of the element and return it
    current_node = self.root
    index = 0
    while current_node is not None:
        if current_node.element == element:
            return index
        current_node = current_node.next
        index += 1
    return -1

  def length(self): # return the length of the list
    count = 0
    n = self.root
    while n is not None:
        n = n.next
        count += 1
    return count

  def __str__(self):
    output = []
    node = self.root
    while node != None:
        output.append(str(node.element))
        node = node.next
    return ' -> '.join(output)

nums = LinkedList()
nums.append(5)
nums.append(6)
nums.append(7)
nums.append(8)
print(nums)
nums.insert(0, 7)
print(nums)


'''
print(nums) # [7, 5, 6]
print(nums.find(5)) # 0
print(nums.find(6)) # 1
print(nums.find(7)) # 2
nums.remove(5)
print(nums) # [7, 6]
print(nums.length()) # 2
'''

