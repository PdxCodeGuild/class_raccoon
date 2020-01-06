


class Node:
    def __init__(self, element, next):
        self.element = element
        self.next = next

    def __str__(self):
        return f'({self.element}, {self.next is not None})'



# a = Node('apple')
# a.next = Node('banana')
# a.next.next = Node('cherry')
#
# # insert avocado at the start
# a = Node('avocado', a)
#
#
# # add kiwi to the end
# last_node = a
# while last_node.next is not None:
#     last_node = last_node.next
# last_node.next = Node('kiwi')
#
#
# node = a
# while node != None:
#     print(node.element, end=' ')
#     node = node.next
# print()


# implementation with nodes
class Stack:
    def __init__(self):
        self.root = None

    def push(self, element): # insert an element at the start (new root)
        self.root = Node(element, self.root)

    def pop(self): # remove an element from the start (the root becomes the next node)
        if self.root is None:
            return None
        first_node = self.root
        self.root = self.root.next
        return first_node.element

    def peek(self): # returns the element on the root node or None if there is no root
        if self.root is None:
            return None
        return self.root.element

    def __len__(self): # return the number of elements
        counter = 0
        node = self.root
        while node != None:
            node = node.next
            counter += 1
        return counter

    def __getitem__(self, i):
        counter = 0
        node = self.root
        while node != None:
            if counter == i:
                return node.element
            node = node.next
            counter += 1
        return None

    def __str__(self):
        output = []
        node = self.root
        while node != None:
            output.append(node.element)
            node = node.next
        return str(output)

    def __repr__(self):
        return self.__str__()


# str/repr =====================================================================
# import datetime
# print(repr(datetime.datetime(2020, 1, 5)))
#
# dates = [datetime.datetime(2020, 1, 5), datetime.datetime(2020, 1, 6)]
# print(dates)

# o = datetzime.datetime(2020, 1, 5)
# exec('o_clone = '+repr(o))
# print(o_clone)

# stacks = [Stack(), Stack(), Stack()]
# print(stacks)

# =====================================

s = Stack() # FILO
s.push(5)
s.push(6)
s.push(7)
s.push(8)
print(len(s))
print(s[0])
print(s[1])
for i in range(len(s)):
    print(s[i])
# print(s)
# print(s.length()) # 2
# print(s.pop()) # 6
# print(s.pop()) # 5

# implementation with lists =====================================
class StackList:
    def __init__(self):
        self.root = None

    def push(self, element): # insert an element at the start (new root)
        self.root = [element, self.root]

    def pop(self): # remove an element from the start (the root becomes the next node)
        if self.root is None:
            return None
        first_node = self.root
        self.root = self.root[1]
        return first_node[0]

    def peek(self): # returns the element on the root node or None if there is no root
        if self.root is None:
            return None
        return self.root[0]

    def __len__(self): # return the number of elements
        counter = 0
        node = self.root
        while node != None:
            node = node[1]
            counter += 1
        return counter

    def __getitem__(self, i):
        counter = 0
        node = self.root
        while node != None:
            if counter == i:
                return node[0]
            node = node[1]
            counter += 1
        return None

    def __str__(self):
        output = []
        node = self.root
        while node != None:
            output.append(node[0])
            node = node[1]
        return str(output)

    def __repr__(self):
        return self.__str__()

sl = StackList()
sl.push(5)
sl.push(6)
sl.push(7)
sl.push(8)
print(sl.root)
sl.pop()
sl.pop()
print(sl.root)




