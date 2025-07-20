class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0


    def get(self, index):
        if index < 0 | index >= self.length:
            return -1

        current = self.head
        for _ in range(index):
            if current is None:
                return -1
            current = current.next
        return current.val if current else -1

    def addAtHead(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def addAtTail(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next

            current.next = new_node
        self.length += 1

    def addAtIndex(self, index, val):
        if index < 0 or index > self.length:
            return
        if index == 0:
            self.addAtHead(val)
            return

        if index == self.length:
            self.addAtTail(val)
            return
        new_node = Node(val)
        current = self.head

        for _ in range(index - 1):
            current = current.next

        new_node.next = current.next
        current.next = new_node
        self.length += 1

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.length:
            return
        if index == 0:
            self.head = self.head.next

        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next

        self.length -= 1


ll = MyLinkedList()
ll.addAtHead(1)  # 1
ll.addAtTail(3)  # 1 -> 3
ll.addAtIndex(1, 2)  # 1 -> 2 -> 3
print(ll.get(1))  # returns 2
ll.deleteAtInde(1)  # 1 -> 3
print(ll.get(1))  # returns 3
