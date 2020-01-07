'''
Filename: data_science.py
Author: Dylan
Purpose: Introduce and practice compsci data structures
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
        self.len = 0 
        # self.new_node = None

    def push(self,element): #insert an element at the start
        self.root = Node(element,self.root)
        self.len += 1
    
    def pop(self): #remove an element from the start
        if self.root is None:
            return None
        ele = self.root.element
        self.root = self.root.next
        self.len -= 1
        return ele


    def peek(self):
        if self.root is None:
            return None
        else:
            return self.root.element

    def length(self):
        return self.len

    def __str__(self): #loops over each element, adds it to a list and then prints the list. 
        output = []
        node = self.root
        while node is not None:
            output.append(str(node.element))
            node = node.next
        return str(output)



# s = Stack()
# s.push(5)
# s.push(6)
# print(s)
# print(s.length()) # 2
# print(s.pop()) # 6
# print(s)

# print(s.pop()) # 5

class LinkedList:
    def __init__(self):
        self.root = None
        self.len = 0 
        self.reference = None

    def push(self,element): #insert an element at the start
        self.root = Node(element,self.root)
        self.len += 1
    
    def pop(self): #remove an element from the start
        if self.root is None:
            return None
        ele = self.root.element
        self.root = self.root.next
        self.len -= 1
        return ele


    def peek(self):
        if self.root is None:
            return None
        else:
            return self.root.element

    def length(self):
        return self.len

    def append(self,element): #add element to the end
        if self.root is None: 
            self.root = Node(element)
        else:
            current_node = self.root #this just goes through the list until the next value is empty
            #which of course means that it's the end of the list
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = Node(element)    
        self.len += 1

    def insert(self,element, idx): #insert element at given index
        self.len += 1
        index = 0 
        if idx == 0: 
            self.push(element)
            return
        current_node = self.root
        while current_node is not None:
            if counter+1 == idx:
                new_node = Node(element, current_node)
                current_node.next = new_node
                break
            index += 1
            current_node = current_node.next
        else:
            self.append(element)
    
    def remove(self,element): #remove the first occurrence of the element
        if self.root is None:
            return
        self.len -= 1
        if self.root == element:
            self.root = self.root.next
            return
        current_node = self.root
        previous_node = None
        while current_node is not None:
            if current_node.element == element:
                previous_node.next = current_node.next
            previous_node = current_node
            current_node = current_node.next

        



    def find(self,element): #find the first occurence of the element
        if self.root is None:
            return None
        index = 0 
        current_node = self.root
        while current_node is not None:
            if current_node.element == element:
                return index
            index += 1
            current_node = current_node.next
        return False
        
    
    def length(self): #return the length of the list
        print(self.len)
        
    def __str__(self):
        output = []
        node = self.root
        while node is not None:
            output.append(str(node.element))
            node = node.next
        return str(output)


nums = LinkedList()
nums.append(5)
nums.append(6)
nums.insert(7, 0)
print(nums) # [7, 5, 6]
print(nums.find(5)) # 1
nums.remove(5)
print(nums) # [7, 6]
print(nums.length()) # 2