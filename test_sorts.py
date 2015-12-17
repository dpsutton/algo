import unittest
import sorts


class TestSorts(unittest.TestCase):

    def test_insertion_emptyinput(self):
        expected = []
        actual = sorts.insertion_sort([])
        self.assertEqual(expected, actual)

    def test_insertion_sort(self):
        numbers = sorts.get_values(20)
        actual = sorts.insertion_sort(numbers)
        expected = sorted(numbers)
        self.assertEqual(expected, actual)

    def test_merge_sort(self):
        size = 170
        values = sorts.get_values(size)
        actual = sorts.merge_sort(values, 0, size - 1)
        expected = sorted(values)
        self.assertEqual(expected, actual)

    def test_merge(self):
        values = [1, 3, 2, 4, 5]
        sorts.merge(values, 0, 2, 4)
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(values, expected)

    def test_merge_biglist(self):
        size = 300
        left = sorted(sorts.get_values(size))
        right = sorted(sorts.get_values(size))
        values = left + right
        expected = sorted(values)

        sorts.merge(values, 0, size, 2 * size - 1)
        self.assertEqual(expected, values)


if __name__ == '__main__':
    unittest.main()
