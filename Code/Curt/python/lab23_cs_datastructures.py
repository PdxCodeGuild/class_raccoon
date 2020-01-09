#stacknode.py
class Node:
    def __init__(self, element, next=None):
        self.element = element
        self.next = next

    def __str__(self):
        return f'({self.element}, {self.next is not None})'

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

class LinkedList:
  def __init__(self):
    self.root = None
  def append(element): # add the element to the end
    if self.root == None:
        self.root = element
    else:
        self.root = self.root + element
  def insert(element, index): # insert the element at the given index
    if index == 0:
        self.root = Node(element, self.root)
        return
    current_node = self.root
    counter = 0
    while current_node is not None:
        if counter == index - 1:
            #create a new node containing element
            #set next node of the new node equal to the next node of the current node
            new_node = Node(element, current_node.next)
            #set the next node of the current node equal to the new node
            current_node.next = new_node
            break

        counter += 1
        current_node = current_node.next
    else:
        self.append(element)

  def remove(self, element): # remove the first occurrence of the element
    #if the list has no elements, just leave
    if self.root is None:
        return
    #if the first node is the one we want to remove
    #update self.root and leave
    if self.root is not None and self.root.element == element:
        self.root = self.root.next
        return
    #otherwise find the node which contains the elements we're removing
    #maintain a reference to the current and previous node
    current_node = self.root
    previous_node = None
    while current_node is not None:
        if current_node.element == element:
            previous_node.next = current_node.next
            break
        previous_node = current_node
        current_node = current_node.next
    #
    # current_node = self.root
    # while current_node.next.element != element:
    #     eat shit and die

  def find(element): # find the first occurrence of the element and return it
    current_node = self.root
    index = 0
    while current_node is not None:
        if current_node.element == element:
            return index
        current_node = current_node.next

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
        return ' -> '.joint(output)

nums = LinkedList()
for i in range(10):
    nums.append(i)

print(nums)
nums.insert('hi', 0)
print(nums)
nums.insert('hello', 4)
print(nums)
nums.insert('goodbye', 1000)
print(nums)
nums.insert('crash', -1)
print(nums)

# nums.insert(7, 0)
# print(nums) # [7, 5, 6]
# print(nums.find(5)) # 1
# nums.remove(5)
# print(nums) # [7, 6]
# print(nums.length()) # 2