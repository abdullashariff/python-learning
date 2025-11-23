class Node: 
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedListStack:

    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node 
        self.size += 1
    
    def pop(self):
        data = self.top.data
        self.top = self.top.next
        self.size -=1
        return data
    
    def isEmpty(self):
        return self.top is None
        

linkedListStack = LinkedListStack()
linkedListStack.push(2)
linkedListStack.push(3)
current = linkedListStack.top
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")