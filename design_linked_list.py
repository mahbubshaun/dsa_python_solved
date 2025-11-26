class ListNode:
    """Node class for the linked list"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:
    """Implementation of a singly linked list with a dummy head node"""

    def __init__(self):
        """Initialize the linked list with a dummy head and size counter"""

        self.dummy_head = ListNode()
        self.size = 0

    def get(self, index: int) -> int:
        """Get the value of the node at the given index. Returns -1 if the index is invalid
        Args:
            index: The index of the node to retrieve (0-indexed)

        :return: The value at the given index, or -1 if the index is invalid

        """

        #Check if index is valid
        if index < 0 or index >= self.size:
            return -1

        #Traverse to target node
        current = self.dummy_head.next
        for _ in range(index):
            current = current.next

        print('Returning value', current.val)
        return current.val


    def addAtIndex(self, index: int, val: int) -> None:

        #if index is invalid, do nothing
        if index > self.size:
            return

        if index <0:
            index = 0
        predecessor = self.dummy_head
        for _ in range(index):
            predecessor = predecessor.next

        new_node = ListNode(val, predecessor.next)
        predecessor.next = new_node
        self.size += 1


    def deleteAtIndex(self, index: int) -> None:

        if index <0 or index >= self.size:
            return

        predecessor = self.dummy_head
        for _ in range(index):
            predecessor = predecessor.next

        node_to_delete = predecessor.next
        predecessor.next = node_to_delete.next
        node_to_delete.next = None
        self.size -= 1

    def addAtHead(self, val:int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def printList(self):
        current = self.dummy_head.next
        values = []

        while current:
            values.append(str(current.val))
            current = current.next

        print(" -> ".join(values) if values else "Empty List")

obj = MyLinkedList()
obj.addAtHead(1)
obj.addAtTail(3)
obj.addAtIndex(1, 2)
obj.get(1)
obj.deleteAtIndex(1)
obj.get(1)
obj.printList()
