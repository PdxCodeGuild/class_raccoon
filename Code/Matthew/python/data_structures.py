


class Node:
    def __init__(self, element, next=None):
        self.element = element
        self.next = next

    def __str__(self):
        return f'({self.element}, {self.next is not None})'



a = Node('apple')
a.next = Node('banana')
a.next.next = Node('cherry')

# insert avocado at the start
a = Node('avocado', a)


# add kiwi to the end
last_node = a
while last_node.next is not None:
    last_node = last_node.next
last_node.next = Node('kiwi')


node = a
while node != None:
    print(node.element, end=' ')
    node = node.next
print()





