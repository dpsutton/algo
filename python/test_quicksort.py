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

    def test_partition_checkInvariants(self):
        arr = [4, 5, 2, 6, 7, 3, 9]
        pivot = qs.partition(arr, 0, 6)
        pivotValue = arr[pivot]
        lessThan = [x <= pivotValue for x in arr[1:pivot]]
        self.assertTrue(all(lessThan))

        greaterThan = [x > pivotValue for x in arr[pivot + 1:]]
        self.assertTrue(all(greaterThan))

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

    def test_randomizedquicksort_maintainsinvariants(self):
        arr = self.get_values(200)
        pivot = qs.randomized_partition(arr, 0, 199)
        pivotValue = arr[pivot]
        lessThan = [x <= pivotValue for x in arr[0:pivot]]
        self.assertTrue(all(lessThan))

        greaterThan = [x > pivotValue for x in arr[pivot + 1:]]
        self.assertTrue(all(greaterThan))

    def test_tailRecursiveQuickSort_correctlySortsValues(self):
        arr = self.get_values(200)
        expected = sorted(arr)
        qs.tailRecursiveQuicksort(arr, 0, 199)
        self.assertEqual(expected, arr)

    def test_make_intervals_works(self):
        intervals = qs.make_intervals(10)
        self.assertEqual(len(intervals), 10)
        lengths = [x.length() >= 3 for x in intervals]
        self.assertTrue(all(lengths))

    def test_intervalOverlaps_startsbeforeOther_ChecksEndpoint(self):
        a = qs.Interval(1, 3)
        b = qs.Interval(2, 4)
        self.assertTrue(a.overlaps(b))
        self.assertTrue(b.overlaps(a))

    def test_intervalOverlaps_dontIntersect(self):
        a = qs.Interval(1, 3)
        b = qs.Interval(4, 6)
        self.assertFalse(a.overlaps(b))
        self.assertFalse(b.overlaps(a))

    def test_intervalOverlapsWithSameStartingPoint_returnstrue(self):
        a = qs.Interval(1, 2)
        b = qs.Interval(1, 3)
        self.assertTrue(a.overlaps(b))
        self.assertTrue(b.overlaps(a))

        a = qs.Interval(3, 4)
        b = qs.Interval(2, 5)
        self.assertTrue(a.overlaps(b))
        self.assertTrue(b.overlaps(a))

    def test_containsPointBefore_whenoverlaps_returnsTrue(self):
        a = qs.Interval(1, 3)
        b = qs.Interval(2, 4)
        self.assertTrue(a.containsPointBefore(b))
        self.assertTrue(b.containsPointBefore(a))

    def test_containsPointBefore_withoutOverlap_checksStartPosition(self):
        a = qs.Interval(1, 3)
        b = qs.Interval(5, 7)
        self.assertTrue(a.containsPointBefore(b))
        self.assertFalse(b.containsPointBefore(a))

    def test_fuzzyPartition_ObeysInvariants(self):
        size = 4000
        intervals = qs.make_intervals(size)
        pivot = qs.fuzzyPartition(intervals, 0, size - 1)
        pivotInterval = intervals[pivot]
        lessThan = [x.containsPointBefore(pivotInterval)
                    for x in intervals[1:pivot - 1]]
        self.assertTrue(all(lessThan))

        greaterThan = [pivotInterval.containsPointBefore(x)
                       for x in intervals[pivot + 1:]]
        self.assertTrue(all(greaterThan))

    def test_fuzzyQuickSort_SimpleArray(self):
        high = qs.Interval(8, 9)
        med = qs.Interval(5, 6)
        low = qs.Interval(1, 3)
        intervals = [high, med, low]
        expected = [low, med, high]
        qs.fuzzyQuickSort(intervals, 0, 2)
        self.assertEqual(expected, intervals)

    def test_fuzzyQuickSort_LotsOfValues(self):
        size = 400
        intervals = qs.make_intervals(size)
        qs.fuzzyQuickSort(intervals, 0, size - 1)
        success = [intervals[x].containsPointBefore(intervals[x + 1])
                   for x in range(0, size - 1)]
        self.assertTrue(all(success))
