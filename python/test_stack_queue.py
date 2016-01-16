import unittest
from stack_queue import Stack
from stack_queue import Queue


class StackTests(unittest.TestCase):

    def test_stack_empty_top_returnsTrue(self):
        stack = Stack()
        self.assertTrue(stack.empty)

    def test_canPushAndPop(self):
        stack = Stack()
        stack.push(1)
        out = stack.pop()
        self.assertEqual(1, out)

    def test_emptyStack_popRaisesException(self):
        stack = Stack()
        self.assertRaises(Exception, stack.pop)

    def test_pushMultiple_ComeOutFILO(self):
        stack = Stack()
        stack.push(2)
        stack.push(1)
        out1 = stack.pop()
        out2 = stack.pop()
        self.assertEqual(1, out1)
        self.assertEqual(2, out2)


class TestQueue(unittest.TestCase):

    def test_emptyQueue_returnsTrueForEmpty(self):
        q = Queue()
        self.assertTrue(q.empty)

    def test_emptyQueue_ThrowsErrorOnDequeue(self):
        q = Queue()
        self.assertRaises(Exception, q.dequeue)

    def test_QueuesInRightOrder(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        first = q.dequeue()
        second = q.dequeue()
        self.assertEqual(1, first)
        self.assertEqual(2, second)


if __name__ == '__main__':
    unittest.main()
