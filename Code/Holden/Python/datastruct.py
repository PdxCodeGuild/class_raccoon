
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

    def __len__(self):
        return self.len

    def append(self, element):
        self.last.next = Node(element)
        self.last = self.last.next
        self.len += 1

    def insert(self, element, index):
        if index - 1 > self.len or index < 0:
            print("index out of range")
            exit()
        current_node = self.root
        for i in range(index):
            prev_node = current_node
            current_node = current_node.next
        prev_node.next = Node(element, current_node)
        if index == self.len:
            self.last = self.last.next
        self.len += 1

    def remove(self, element):
        current_node = self.root
        prev_node = current_node
        for i in range(self.len):
            if current_node.element == element:
                prev_node.next = current_node.next
                if i == 0:
                    self.root = current_node.next
                if current_node.next == None:
                    self.root = None
                    self.last = None
                elif i == self.len-1:
                    self.last = prev_node
                self.len -= 1
                break
            prev_node = current_node
            current_node = current_node.next
        else:
            print("element not in list")

    def find(self, element):
        current_node = self.root
        for i in range(self.len):
            if current_node.element == element:
                return i
            current_node = current_node.next
        else:
            return -1

    def __str__(self):
        output = "["
        current_node = self.root
        for i in range(self.len-1):
            output += str(current_node.element) + ", "
            current_node = current_node.next
        output += str(current_node.element) + "]"
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
print(f'\"end?\" found at {teststack.find("end?")}')
print(teststack)
print(teststack.length())
print(teststack.pop())
print(teststack.length())
for i in range(teststack.len):
    print(teststack.pop())
