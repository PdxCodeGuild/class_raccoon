#Computer science lab with NodEs 

# class StackList:
#     def __init__(self):
#         self.root = None
#     def push(self, element):
#         self.root = [element, self.root]
#     def pop(self):
#         if self.root is None:
#             return None
#         first_node = self.root
#         self.root = self.root[1]
#         return first_node[0]
#     def peek(self):
#         if self.root is None:
#             return None
#         return self.root
#     def __len__(self):
#         counter = 0
#         node = self.root
#         while node != None: 
#             node = node[1]
#             counter += 1
#         return counter
#     def __getitem__(self,i):
#         counter = 0 
#         node = self.root
#         while node != None:
#             if counter == i:push
#         return node[0]
#         node = node[1]
#             counter += 1
#         return None

# 
        


class Node:
    def __init__(self, element, next=None):
        self.element = element
        self.next = next

    def __str__(self):
        return f'({self.element}, {self.next is not None})'

class LinkedList:
    
    def __init__(self):
        self.root = None
        self.tail = None
    def push(self,element):
        self.root = Node(element,self.root)
    def append(self, element):
        if self.root == None:
            self.tail = Node(element)
            self.root  = self.tail
        else:
            self.tail.next = Node(element)
            
            
    def insert(element,index):
        for i in self.root:
            self.root 
    def remove(self, element):
        pass
    def find(self, element):
        pass
    def length(self, element):
        count = 0 
        n = self.node.next
        while n != None:
            n = n.next
            count += 1
        return count
        
    def __str__(self):
        output = []
        node = self.root
        while node != None:
            output.append(node.element)
            node = node.next
        return str(output)
    def __repr__(self):
        return self.__str__()
        
        
        
        
        
        
        
        
ll = LinkedList()
ll.append(5)
ll.append(6)
ll.append(7)
ll.append(8)
print(ll)
# ll.pop()
# ll.pop()
# print(ll.root)

# class Node:
#     def __init__(self, element, next):
#         self.element = element
#         self.next = next
# ​
#     def __str__(self):
#         return f'({self.element}, {self.next is not None})'
# ​
# ​
# ​
# # a = Node('apple')
# # a.next = Node('banana')
# # a.next.next = Node('cherry')
# #
# # # insert avocado at the start
# # a = Node('avocado', a)
# #
# #
# # # add kiwi to the end
# # last_node = a
# # while last_node.next is not None:
# #     last_node = last_node.next
# # last_node.next = Node('kiwi')
# #
# #
# # node = a
# # while node != None:
# #     print(node.element, end=' ')
# #     node = node.next
# # print()
# ​
# ​
# # implementation with nodes
# class Stack:
#     def __init__(self):
#         self.root = None
# ​
#     def push(self, element): # insert an element at the start (new root)
#         self.root = Node(element, self.root)
# ​
#     def pop(self): # remove an element from the start (the root becomes the next node)
#         if self.root is None:
#             return None
#         first_node = self.root
#         self.root = self.root.next
#         return first_node.element
# ​
#     def peek(self): # returns the element on the root node or None if there is no root
#         if self.root is None:
#             return None
#         return self.root.element
# ​
#     def __len__(self): # return the number of elements
#         counter = 0
#         node = self.root
#         while node != None:
#             node = node.next
#             counter += 1
#         return counter
# ​
#     def __getitem__(self, i):
#         counter = 0
#         node = self.root
#         while node != None:
#             if counter == i:
#                 return node.element
#             node = node.next
#             counter += 1
#         return None
# ​
#     def __str__(self):
#         output = []
#         node = self.root
#         while node != None:
#             output.append(node.element)
#             node = node.next
#         return str(output)
# ​
#     def __repr__(self):
#         return self.__str__()
# ​
# ​
# # str/repr =====================================================================
# # import datetime
# # print(repr(datetime.datetime(2020, 1, 5)))
# #
# # dates = [datetime.datetime(2020, 1, 5), datetime.datetime(2020, 1, 6)]
# # print(dates)
# ​
# # o = datetzime.datetime(2020, 1, 5)
# # exec('o_clone = '+repr(o))
# # print(o_clone)
# ​
# # stacks = [Stack(), Stack(), Stack()]
# # print(stacks)
# ​
# # =====================================
# ​
# s = Stack() # FILO
# s.push(5)
# s.push(6)
# s.push(7)
# s.push(8)
# print(len(s))
# print(s[0])
# print(s[1])
# for i in range(len(s)):
#     print(s[i])
# # print(s)
# # print(s.length()) # 2
# # print(s.pop()) # 6
# # print(s.pop()) # 5
