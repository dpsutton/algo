import unittest
import linearTime as lt
import random as r


class TestLinearTime(unittest.TestCase):

    def get_integers(self, size, max):
        return [r.randint(0, max) for _ in range(size)]

    def test_countingSort(self):
        initial = [2, 5, 3, 0, 2, 3, 0, 3]
        expected = sorted(initial)
        actual = lt.countingSort(initial, 5)
        self.assertEqual(expected, actual)

    def test_countingSort_biggerArray(self):
        initial = self.get_integers(200, 200)
        expected = sorted(initial)
        actual = lt.countingSort(initial, 200)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
