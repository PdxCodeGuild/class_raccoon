#Computer science lab with NodEs 


class Node:
    def __init__(self, element, next=None):
        self.element = element
        self.next = next

class Stack:
    def __init__(self):
        self.root = None
    def push(self, element): # insert an element at the start
        self.root = Node(element, self.root)
    def pop(self, element): # remove an element from the start
        # for i in Node(element,self.root):
        pass
    def length(self): # return the number of elements
        pass
    def __str__(self):
        return f"{self.element}{self.next}"

s = Stack()

s.push(5)
s.push(6)
s.push(7)

# print(s.length()) # 2
# # print(s.pop()) # 6
# # print(s.pop()) # 5

node = s.root
while node != None:
    print(node.element,  end=' ')
    node = node.next
print()
