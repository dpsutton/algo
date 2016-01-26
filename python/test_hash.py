import unittest
import myhash as h
import random


class TestHash(unittest.TestCase):

    def test_hashChainsOnCollisions(self):
        size = 10
        hash = h.chainedHash(size)
        index = id(1) % size
        hash.insert(1)
        self.assertEqual(1, hash.keys[index].nil.next.val)

    def test_checkLengths(self):
        """if we use a non-prime key, we get clumping. We stay i nthe even
values. Possibly a word alignment issue. But there are no value types
so i can't see word size. ha, neat. pointers are byte aligned to 16
bytes unless id() is lying to me (ie, does it return a virtual memory
address or some kind of internal structure "memory location"

        """
        size = 16
        hash = h.chainedHash(size)
        for i in range(8000):
            hash.insert(complex(random.random(), random.random()))
            # hash.insert(i)
        for i in range(len(hash.keys)):
            print "size of bucket {}: {}".format(i, hash.keys[i].length())


if __name__ == '__main__':
    unittest.main()
