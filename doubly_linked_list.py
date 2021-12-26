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


linked_list = DoublyLinkedList()
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
assert linked_list.tail.data == "Item 6"
assert linked_list.size == 4
