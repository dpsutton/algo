class LinkedList(object):
    """Linked List class that adds objects as nodes. It is doubly linked
and uses a nil pointer for ease.

    """

    def __init__(self):
        super(LinkedList, self).__init__()
        self.nil = Node("nil")
        self.nil.next = self.nil.previous = self.nil

    def add(self, val):
        "add the new value at the head of the list"
        node = Node(val)
        node.next = self.nil.next
        node.previous = self.nil.next
        self.nil.next = node

    def remove(self, node):
        "remove a node (by reference) from the linked list"
        node.previous.next = node.next
        node.next.previous = node.previous

    def find(self, key):
        current = self.nil.next
        while current != self.nil and current.val != key:
            current = current.next
        return current

    def length(self):
        length = 0
        current = self.nil.next
        while current != self.nil:
            length = length + 1
            current = current.next
        return length


class Node(object):
    """Doubly linked Node for linked lists

    """

    def __init__(self, val):
        super(Node, self).__init__()
        self.val = val
        self.next = None
        self.previous = None
