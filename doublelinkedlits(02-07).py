# ==========================================
# Day 10 - Doubly Linked List
# Date: 02-07-2026
# ==========================================

class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None

    # -------------------------
    # Insert at Beginning
    # -------------------------
    def insert_begin(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    # -------------------------
    # Insert at End
    # -------------------------
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    # -------------------------
    # Insert at Position
    # -------------------------
    def insert_position(self, pos, data):

        if pos == 0:
            self.insert_begin(data)
            return

        new_node = Node(data)
        temp = self.head

        for i in range(pos - 1):
            if temp is None:
                print("Invalid Position")
                return
            temp = temp.next

        if temp is None:
            print("Invalid Position")
            return

        new_node.next = temp.next
        new_node.prev = temp

        if temp.next:
            temp.next.prev = new_node

        temp.next = new_node

    # -------------------------
    # Delete at Beginning
    # -------------------------
    def delete_begin(self):

        if self.head is None:
            print("List is Empty")
            return

        if self.head.next is None:
            self.head = None
            return

        self.head = self.head.next
        self.head.prev = None

    # -------------------------
    # Delete at End
    # -------------------------
    def delete_end(self):

        if self.head is None:
            print("List is Empty")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.prev.next = None

    # -------------------------
    # Delete at Position
    # -------------------------
    def delete_position(self, pos):

        if self.head is None:
            print("List is Empty")
            return

        if pos == 0:
            self.delete_begin()
            return

        temp = self.head

        for i in range(pos):
            if temp is None:
                print("Invalid Position")
                return
            temp = temp.next

        if temp is None:
            print("Invalid Position")
            return

        if temp.next:
            temp.next.prev = temp.prev

        temp.prev.next = temp.next

    # -------------------------
    # Display Forward
    # -------------------------
    def display_forward(self):

        temp = self.head

        print("Forward Traversal:")

        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")

    # -------------------------
    # Display Backward
    # -------------------------
    def display_backward(self):

        if self.head is None:
            print("List is Empty")
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        print("Backward Traversal:")

        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev

        print("None")


# ==========================================
# Driver Code
# ==========================================

dll = DoublyLinkedList()

# Insert at End
dll.insert_end(10)
dll.insert_end(20)
dll.insert_end(30)

dll.display_forward()

# Insert at Beginning
dll.insert_begin(5)

dll.display_forward()

# Insert at Position
dll.insert_position(2, 15)

dll.display_forward()

# Backward Traversal
dll.display_backward()

# Delete at Beginning
dll.delete_begin()

dll.display_forward()

# Delete at End
dll.delete_end()

dll.display_forward()

# Delete at Position
dll.delete_position(1)

dll.display_forward()