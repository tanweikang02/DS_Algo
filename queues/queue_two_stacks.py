# Queue implemented with 2 Stacks data structure


# ================================================================================

# Stack Implementation

# ================================================================================


class Stack:
    def __init__(self):
        self.data = []
        self.size = 0
        self.max_capacity = 3

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
            self.size -= 1
            return self.data.pop()

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


# ================================================================================

# Queue Implementation

# ================================================================================


class Queue:
    def __init__(self):
        self.enqueue_stack = (
            Stack()
        )  # All items'll be positioned in this stack after enqueue() operation
        self.dequeue_stack = (
            Stack()
        )  # All items'll be positioned in this stack after dequeue() operation

    def enqueue(self, data):
        if (self.dequeue_stack.size < self.dequeue_stack.max_capacity) and (
            self.enqueue_stack.size < self.enqueue_stack.max_capacity
        ):
            if self.dequeue_stack.is_empty != True:
                while self.dequeue_stack.size > 0:
                    self.enqueue_stack.push(self.dequeue_stack.pop())
            self.enqueue_stack.push(data)
        else:
            print("Error: Queue Overflow")

    def dequeue(self):
        if (self.dequeue_stack.size + self.enqueue_stack.size) > 0:
            if self.enqueue_stack.is_empty != True:
                while self.enqueue_stack.size > 0:
                    self.dequeue_stack.push(self.enqueue_stack.pop())
            self.dequeue_stack.pop()
        else:
            print("Error: Queue Underflow")


# Test cases

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.dequeue()
queue.enqueue(6)
queue.dequeue()

assert queue.enqueue_stack.peek() == None
assert queue.dequeue_stack.peek() == 3

# Expected Output: print 'Queue Overflow' twice, A 'stack is empty' message will also be printed.
# And no errors arise.
