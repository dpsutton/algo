import linked_list as l


class chainedHash(object):
    """Documentation for chainedHash

    """

    def __init__(self, size=10):
        super(chainedHash, self).__init__()
        self.keys = []
        self.size = size
        for _ in range(size):
            self.keys.append(l.LinkedList())

    def insert(self, val):
        index = id(val) % self.size
        self.keys[index].add(val)
