class Stack(object):
    """Naive stack implementation

    """

    def __init__(self):
        super(Stack, self).__init__()
        self.stack = []

    def empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.empty():
            raise Exception("underflow")
        elem = self.stack[-1]
        self.stack = self.stack[:-1]
        return elem


class Queue(object):
    """Naive queue for testing

    """

    def __init__(self):
        super(Queue, self).__init__()
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def enqueue(self, item):
        self.elements.append(item)

    def dequeue(self):
        if self.empty():
            raise Exception("underflow")
        elem = self.elements[0]
        self.elements = self.elements[1:]
        return elem
