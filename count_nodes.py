class Node:
    def __init__(self, new_data):

        self.data = new_data
        self.next = None

def count_nodes(head):
    count = 0
    curr = head

    while curr is not None:
        count += 1

        curr = curr.next
    return count

def printList(node):
    while node is not None:
        print(f"{node.data}", end="")
        if node.next is not None:
            print("->", end="")
        node = node.next
    print()

def searchInLinkedList(node, key):
    while node is not None:
        print(node.data)
        if node.data == key:
            print('Found!')
            break
        node = node.next


def insertAtFront(node, value):
    newNode = Node(value)
    newNode.next = node
    return newNode


def insert_after(node, key, new_data):
    new_node = Node(new_data)
    curr = node
    while curr is not None:
        if key == curr.data:
            print('Found the given node', curr.data)
            break
        curr = curr.next

    if curr is None:
        print('Node not found')
        return head

    new_node.next = curr.next

    curr.next = new_node

    return node


if __name__ == "__main__":
    # head = Node(1)
    # head.next = Node(3)
    # head.next.next = Node(1)
    # head.next.next.next= Node(2)
    # head.next.next.next.next = Node(1)
    # head = Node(10)
    # head.next = Node(20)
    # head.next.next = Node(30)
    # head.next.next.next = Node(40)

    # print("count of nodes is", count_nodes(head))
    # printList(head)
    # head = Node(1)
    # head.next = Node(2)
    # head.next.next = Node(3)
    # head.next.next.next = Node(4)
    # head.next.next.next.next = Node(5)

    # searchInLinkedList(head, 5)

    # head = Node(2)
    # head.next = Node(3)
    # head.next.next = Node(4)
    # head.next.next.next = Node(5)
    # x = 1
    # head = insertAtFront(head, x)
    # printList(head)

    head = Node(2)
    head.next = Node(3)
    head.next.next = Node(5)
    head.next.next.next = Node(6)

    print("Original Linked List: ", end="")
    printList(head)

    # Key: Insert node after key
    key = 3
    new_data = 4

    head = insert_after(head, key, new_data)

    printList(head)



