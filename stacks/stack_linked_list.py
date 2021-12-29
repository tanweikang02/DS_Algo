# Stack implemented with previously-built Doubly Linked List

# =======================================================================================

# Doubly Linked List Implementation

# ======================================================================================


class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        node = Node(data)

        if self.head == None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

        self.size += 1

    def delete(self, data):
        curr = self.head
        while curr != None:
            if curr.data == data:
                if curr == self.head:
                    self.head = curr.next
                    curr.next.prev = None
                elif curr == self.tail:
                    self.tail = curr.prev
                    curr.prev.next = None
                else:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev

                self.size -= 1
                return

            curr = curr.next


# =============================================================================

# Stack Implementation

# =============================================================================


class Stack:
    def __init__(self):
        self.data = DoublyLinkedList()
        self.max_capacity = 10

    def push(self, data):
        if self.data.size < 10:
            self.data.append(data)
        else:
            print("Error: StackOverFlow")

    def pop(self):
        if self.data.head != None:
            self.data.delete(self.data.tail.data)
        else:
            print("Error: StackUnderFlow")

    def peek(self):
        return self.data.tail.data

    def is_empty(self):
        return self.data.head == None

    def is_full(self):
        return self.data.size == 10


# Test cases

stack = Stack()
stack.is_empty()
for i in range(11):
    stack.push(i)
assert stack.peek() == 9
stack.pop()
stack.pop()
assert stack.peek() == 7
