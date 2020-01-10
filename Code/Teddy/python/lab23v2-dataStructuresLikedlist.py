'''
Computer Science - Data Structures
Version 2 - Linked List
A linked list is like a regular list in Python, and provides methods for adding and removing elements.

Stub:

class LinkedList:
  def __init__(self):
    self.root = None
  def append(self, element): # add the element to the end
    ...
  def insert(self, element, index): # insert the element at the given index
    ...
  def remove(self, element): # remove the first occurrence of the element
    ...
  def find(self, element): # find the first occurrence of the element and return it
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
class Node:
    def __init__(self, element, next=None):
        self.element = element
        self.next = next

    def __str__(self):
        return f'({self.element}, {self.next is not None})'


class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, element): # add an element to the start
        self.head = Node(element, self.head)

    def pop(self): # remove an element from the start (the root becomes the next node)
        if self.head is None:
            return None
        first_node = self.head
        self.head = self.head.next
        return first_node.element

    def peek(self): # returns the element on the root node or None if there is no root
        if self.head is None:
            return None
        return self.head.element

    def append(self, element): # add the element to the end
        new_node = Node(element)
        if self.head is None:
            self.head = new_node
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = new_node

    def insert(self, element, index): # insert the element at the given index
        if index == 0:
            self.push(element)
            return
        current_node = self.head
        counter = 0
        while current_node is not None:
            if counter ==index-1:
                new_node = Node(element, current_node.next)
                current_node.next = new_node
                break
            counter += 1
            current_node = current_node.next


    def remove(self, element): # remove the first occurrence of the element
        # if the list has no elements
        if self.head is None:
            # leave
            return
        # if the first node is the one we want to remove
        if self.head is not None and self.head.element == element:
            # update self.root to the next node
            self.head = self.head.next
            # leave
            return

        # otherwise find the node which contains the element we're removing
        # maintain a reference to the current and previous node
        current_node = self.head
        previous_node = None
        # Not an empty list
        while current_node is not None:
            #if found the element
            if current_node.element == element:
                #link the previous node to the next node
                previous_node.next = current_node.next
                # leave a program
                break
            previous_node = current_node
            current_node = current_node.next

    def find(self, element): # find the first occurrence of the element and return the index
        current_node = self.head
        index = 0

        while current_node is not None:
            if current_node.element == element:
                return index
            current_node = current_node.next
            index += 1
        return -1

    def length(self): # return the length of the list
        count = 0
        node = self.head
        while node is not None:
            node = node.next
            count += 1
        return count

    def __str__(self):
        output = []
        node = self.head
        while node is not None:
            output.append(node.element)
            node = node.next
        return str(output)


nums = LinkedList()
nums.append(5)
nums.append(6)
nums.append(7)
nums.append(8)
print(nums) # [5, 6, 7, 8]

print(f'Length is {nums.length()}') # Length is 4

nums.insert(7, 0)

print(nums) # [7, 5, 6, 8]
print(nums.find(5)) # 1
nums.remove(5)
print(nums) # [7, 6, 7, 8]
print(f'Length is {nums.length()}') # Length is 4
