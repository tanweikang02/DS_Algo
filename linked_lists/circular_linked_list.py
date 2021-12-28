class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        node = Node(data)

        if self.size == 0:
            self.head = node
        elif self.size == 1:
            self.head.next = node
            self.head.prev = node
            node.next = self.head
            node.prev = self.head
        else:
            prev = self.head.prev
            prev.next = node
            self.head.prev = node
            node.next = self.head
            node.prev = prev

        self.size += 1

    def delete(self, data):
        i = 0
        curr = self.head
        while i < self.size:
            if curr.data == data:
                if curr == self.head:
                    self.head = curr.next
                    self.head.prev = curr.prev
                    self.head.prev.next = self.head
                else:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev

            i += 1

        self.size -= 1


linked_list = CircularLinkedList()
linked_list.append("Item 1")
linked_list.append("Item 2")
linked_list.append("Item 3")
linked_list.append("Item 4")
linked_list.append("Item 5")
linked_list.append("Item 6")
linked_list.delete("Item 5")
linked_list.delete("Item 1")

# Test cases

assert linked_list.head.data == "Item 2"
assert linked_list.head.prev.data == "Item 6"
assert linked_list.size == 4
