# Python OOP

# Singly Linked list is a linked list that traverse only in 1 direction. Where there are others like doubly linked list, etc.


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # add data to the end of the linked list.
    def append(self, data):
        node = Node(data)

        # If the list is empty
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    # linearly searches for the data, if found, make the previous node point to next node, as if the current node is deleted.
    def delete(self, data):
        current = self.head
        previous = self.head

        while current != None:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                elif current == self.tail:
                    self.tail = previous
                    self.tail.next = None
                else:
                    previous.next = current.next
                print(f"Deleted {data}.")
                self.size -= 1
                return

            previous = current
            current = current.next

        print("Item not found!")


linked_list = SinglyLinkedList()
linked_list.append("Item 1")
linked_list.append("Item 2")
linked_list.append("Item 3")
linked_list.append("Item 4")
linked_list.append("Item 5")
linked_list.append("Item 6")
linked_list.delete("Item 5")


# Test cases

assert linked_list.head.data == "Item 1"
assert linked_list.head.next.data == "Item 2"
assert linked_list.tail.data == "Item 6"
assert linked_list.tail.next == None
assert linked_list.size == 5
