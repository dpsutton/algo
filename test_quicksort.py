import unittest
import random
import quicksort as qs


class TestQuickSort(unittest.TestCase):

    def get_values(self, size):
        return [random.randint(1, 100000) for _ in range(size)]

    def test_partition_simpleValue_setsPivot(self):
        arr = [1, 2, 3, 4, 5, 6]
        expected = [1, 2, 3, 4, 5, 6]
        pivot = qs.partition(arr, 0, 5)
        self.assertEqual(expected, arr)
        self.assertEqual(pivot, 5)

    def test_partition_singleValue_returnsSingleValue(self):
        arr = [1]
        pivot = qs.partition(arr, 0, 0)
        self.assertEqual(pivot, 0)

    def test_partition_simpleValues_SwapsValues(self):
        arr = [5, 9, 3, 2, 8, 6]
        expected = [5, 3, 2, 6, 8, 9]
        pivot = qs.partition(arr, 0, 5)
        self.assertEqual(expected, arr)
        self.assertEqual(pivot, 3)

    def test_quicksort_simplearray_sorts(self):
        arr = [5, 9, 3, 2, 8, 6]
        qs.quicksort(arr, 0, 5)
        expected = sorted(arr)
        self.assertEqual(expected, arr)

    def test_quicksort_lotsofvalues_sortsarray(self):
        arr = self.get_values(300)
        qs.quicksort(arr, 0, 299)
        expected = sorted(arr)
        self.assertEqual(expected, arr)
