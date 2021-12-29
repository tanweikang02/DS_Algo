# Queue implemented with Python List


class Queue:
    def __init__(self):
        self.data = []
        self.size = 0
        self.max_capacity = 10

    def enqueue(self, data):
        if self.size < self.max_capacity:
            self.data.append(data)
            self.size += 1
        else:
            print("Error: Queue Overflow")

    def dequeue(self):
        if self.size > 0:
            self.data.pop(0)
            self.size -= 1
        else:
            print("Error: Queue Underflow")

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.max_capacity


# Test cases

queue = Queue()
for i in range(12):
    queue.enqueue(i)
assert queue.is_full() == True
assert queue.is_empty() == False
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
assert queue.data[0] == 4
assert queue.is_full() == False

# Expected output: print 'Queue Overflow' twice. And no errors arise.
