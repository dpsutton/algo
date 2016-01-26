import unittest
import linked_list as l


class TestLinkedList(unittest.TestCase):

    def test_linkedlist_createsnil(self):
        linked = l.LinkedList()
        self.assertEqual(linked.nil.next, linked.nil)
        self.assertEqual("nil", linked.nil.val)

    def test_linked_list_can_add_node(self):
        linked = l.LinkedList()
        linked.add(3)
        self.assertEqual(3, linked.nil.next.val)
        self.assertEqual(1, linked.length())

    def test_remove_can_remove_item(self):
        linked = l.LinkedList()
        self.assertEqual(0, linked.length())
        linked.add(1)
        self.assertEqual(1, linked.length())
        linked.remove(linked.nil.next)
        self.assertEqual(0, linked.length())

    def test_finds_by_key(self):
        linked = l.LinkedList()
        size = 200
        for i in range(size):
            linked.add(i)
        self.assertEqual(size, linked.length())
        found = linked.find(size / 2)
        self.assertEqual(size / 2, found.val)

    def test_whenNotFound_returns_linkedNil(self):
        linked = l.LinkedList()
        size = 200
        for i in range(size):
            linked.add(i)
        self.assertEqual(size, linked.length())
        found = linked.find(size * 2)
        self.assertEqual("nil", found.val)


if __name__ == '__main__':
    unittest.main()
