# implementation with lists =====================================
class StackList:
    def __init__(self):
        self.root = None
​    def push(self, element): # insert an element at the start (new root)
        self.root = [element, self.root]
​    def pop(self): # remove an element from the start (the root becomes the next node)
        if self.root is None:
            return None
            first_node = self.root
            self.root = self.root[1]
            return first_node[0]
​    def peek(self): # returns the element on the root node or None if there is no root
        if self.root is None:
            return None
            return self.root[0]
​    def __len__(self): # return the number of elements
        counter = 0
        node = self.root
        while node != None:
            node = node[1]
            counter += 1
            return counter
​    def __getitem__(self, i):
        counter = 0
        node = self.root
        while node != None:
        if counter == i:
            return node[0]
            node = node[1]
            counter += 1
            return None
​    def __str__(self):
        output = []
        node = self.root
        while node != None:
            output.append(node[0])
            node = node[1]
            return str(output)
​    def __repr__(self):
        return self.__str__()
​
sl = StackList()
sl.push(5)
sl.push(6)
sl.push(7)
sl.push(8)
print(sl.root)
sl.pop()
sl.pop()
print(sl.root)
​