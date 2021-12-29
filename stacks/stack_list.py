# Stack implemented with Python List


class Stack:
    def __init__(self):
        self.data = []
        self.size = 0
        self.max_capacity = 10

    def push(self, data):
        if self.size < self.max_capacity:
            self.data.append(data)
            self.size += 1
        else:
            print("Error: StackOverFlow")

    def pop(self):
        if self.size == 0:
            print("Error: StackUnderFlow")
        else:
            self.data.pop()
            self.size -= 1

    def peek(self):
        if self.size > 0:
            return self.data[-1]
        print("The stack is empty. Nothing will be returned.")

    def is_empty(self):
        if self.size == 0:
            return True
        return False

    def is_full(self):
        if self.size == self.max_capacity:
            return True
        return False


# Test cases

stack = Stack()
stack.is_empty()
for i in range(11):
    stack.push(i)
assert stack.peek() == 9
stack.pop()
stack.pop()
assert stack.peek() == 7

# Expected output: print 'Queue Overflow' once. And no errors arise.
