
class Node:
    def __init__(self, element, next=None):
        self.element = element
        self.next = next
    def __str__(self):
        return str(self)

class Stack:
    def __init__(self):
        self.root=None
        self.len = 0
        self.last=None

    def push(self, element):
        self.root = Node(element, self.root)
        if self.last == None:
            self.last = self.root
        self.len += 1

    def pop(self):
        if self.root == None:
            return None
        output = self.root.element
        self.root = self.root.next
        if self.root == None:
            self.last = None
        self.len -= 1
        return str(output)

    def peek(self):
        return str(self.root.element)

    def length(self):
        return str(self.len)

    def append(self, element):
        self.last.next = Node(element)
        self.last = self.last.next
        self.len += 1

    def insert(self, element, index):
        if index - 1 > self.len:
            print("index out of range")
            exit()
        current_index = self.root
        for i in range(index):
            prev_index = current_index
            current_index = current_index.next
        new_index = Node(element, current_index)
        prev_index.next = new_index
        if index == self.len:
            self.last = self.last.next
        self.len += 1

    def remove(self, element):
        current_index = self.root
        prev_index = current_index
        for i in range(self.len):
            if current_index.element == element:
                prev_index.next = current_index.next
                if i == 0:
                    self. root = current_index.next
                if current_index.next == None:
                    self.root = None
                    self.last = None
                elif i == self.len-1:
                    self.last = prev_index
                self.len -= 1
                break
            prev_index = current_index
            current_index = current_index.next
        else:
            print("element not in list")

    def find(self, element):
        current_index = self.root
        for i in range(self.len):
            if current_index.element == element:
                return i
            current_index = current_index.next
        else:
            return -1

    def __str__(self):
        output = "["
        current_root = self.root
        for i in range(self.len-1):
            output += str(current_root.element) + ", "
            current_root = current_root.next
        output += str(current_root.element) + "]"
        return output

var = "lel"
teststack = Stack()
teststack.push(9)
teststack.push(4)
teststack.push(8)
teststack.push(40)
teststack.push("dumb")
teststack.push(var)
teststack.append("ap")
teststack.insert(8,4)
teststack.push(8)
print(teststack)
teststack.remove(8)
teststack.insert("end?", 8)
teststack.append("end.")
print(teststack.find("end?"))
print(teststack)
print(teststack.length())
print(teststack.pop())
print(teststack.length())
for i in range(teststack.len):
    print(teststack.pop())
