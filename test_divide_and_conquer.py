import unittest
import random
import divide_and_conquer as dac


class TestDivide_And_Conquer(unittest.TestCase):
    def test_find_max_crossing_subarray_allpositive(self):
        arr = [1, 1, 1, 1, 1]
        low = 0
        high = 4
        mid = (high + low) // 2
        expected_sum = high - low + 1
        expected = (low, high, expected_sum)
        actual = dac.find_max_crossing_subarray(arr, low, mid, high)
        self.assertEqual(expected, actual)

    def test_find_max_crossing_subarray_withnegative(self):
        arr = [-7, 4, 1, -6, 2, -4, 10, -9]
        low = 1
        high = 6
        left_sum = -1
        right_sum = 8
        expected = (low, high, left_sum + right_sum)
        actual = dac.find_max_crossing_subarray(arr, 0, 3, 7)
        self.assertEqual(expected, actual)

    def test_maxsubarray_singleelement(self):
        actual = dac.find_max_subarray([3], 0, 0)
        expected = (0, 0, 3)
        self.assertEqual(expected, actual)

    def test_maxsubarray_allpositive(self):
        arr = [1, 1, 1]
        expected = (0, 2, 3)
        actual = dac.find_max_subarray(arr, 0, 2)
        self.assertEqual(expected, actual)

    def test_maxsubarray_allnegative(self):
        arr = [-3, -1, -3]
        expected = (1, 1, -1)
        actual = dac.find_max_subarray(arr, 0, 2)
        self.assertEqual(expected, actual)

    def test_brutemaxarray_singleelement(self):
        actual = dac.brute_maxsubarray([3])
        expected = (0, 0, 3)
        self.assertEqual(expected, actual)

    def test_brutemaxarray_allpositive(self):
        actual = dac.brute_maxsubarray([1, 1, 1, 1])
        expected = (0, 3, 4)
        self.assertEqual(expected, actual)

    def test_brutemaxarray_allNegativeExceptLast(self):
        actual = dac.brute_maxsubarray([-1, -1, -1, 17])
        expected = (3, 3, 17)
        self.assertEqual(expected, actual)

    def test_brutemaxarray_allnegative(self):
        actual = dac.brute_maxsubarray([-3, -1, -3])
        expected = (1, 1, -1)
        self.assertEqual(expected, actual)

    def test_linearmaxarray_singleElement(self):
        actual = dac.linear_maxsubarray([3])
        expected = (0, 0, 3)
        self.assertEqual(expected, actual)

    def test_linearmaxarray_allPositive(self):
        actual = dac.linear_maxsubarray([1, 1, 1])
        expected = (0, 2, 3)
        self.assertEqual(expected, actual)

    def test_linearmaxarray_allnegative(self):
        actual = dac.linear_maxsubarray([-3, -1, -3])
        expected = (1, 1, -1)
        self.assertEqual(expected, actual)

    def test_linearmaxarray_straightforward(self):
        arr = [1, 2, 3, -100, -100]
        actual = dac.linear_maxsubarray(arr)
        expected = (0, 2, 6)
        self.assertEqual(expected, actual)

    def test_linearmaxarray_skipnegatives(self):
        arr = [-4, 1, 1, 2, -4]
        actual = dac.linear_maxsubarray(arr)
        expected = (1, 3, 4)
        self.assertEqual(expected, actual)

    def test_linearmaxarray_knowswhentoend(self):
        arr = [-4, 1, 1, 1, 3, -2, -9]
        actual = dac.linear_maxsubarray(arr)
        expected = (1, 4, 6)
        self.assertEqual(expected, actual)

    def test_linearmaxarray_continuesovernegatives(self):
        arr = [-4, 1, 5, -3, 4, -7]
        actual = dac.linear_maxsubarray(arr)
        expected = (1, 4, 7)
        self.assertEqual(expected, actual)

    def test_maxheapify_OnLeafDoesntExchange(self):
        arr = [0, 15, 4, 3]
        dac.max_heapify(arr, 3)
        expected = [0, 15, 4, 3]
        self.assertEqual(expected, arr)

    def test_maxheapify_OnRootExchanges(self):
        arr = [0, 12, 15, 4]
        dac.max_heapify(arr, 1)
        expected = [0, 15, 12, 4]
        self.assertEqual(expected, arr)

    def test_maxheapify_OnBigArray(self):
        arr = [0, 4, 14, 10, 8, 7, 9, 3, 2, 4, 1]
        dac.max_heapify(arr, 1)
        expected = [0, 14, 8, 10, 4, 7, 9, 3, 2, 4, 1]
        self.assertEqual(expected, arr)

    def test_minheapify_OnLeafDoesntExchange(self):
        arr = [0, 1, 2, 3, 4, 5, 6]
        dac.min_heapify(arr, 6)
        expected = [0, 1, 2, 3, 4, 5, 6]
        self.assertEqual(expected, arr)

    def test_minheapify_OnRootExchanges(self):
        arr = [0, 2, 4, 1]
        dac.min_heapify(arr, 1)
        expected = [0, 1, 4, 2]
        self.assertEqual(expected, arr)

    def test_buildMaxHeap_trivialCase(self):
        arr = [0, 1]
        dac.build_maxHeap(arr)
        expected = [0, 1]
        self.assertEqual(expected, arr)

    def test_buildMaxHeap_threeElement(self):
        arr = [0, 3, 2, 5, 6]
        dac.build_maxHeap(arr)
        expected = [0, 6, 3, 5, 2]
        self.assertEqual(expected, arr)

    def test_heapsort_SimpleExample(self):
        arr = [3, 5, 2, 9]
        actual = dac.heapsort(arr)
        expected = [2, 3, 5, 9]
        self.assertEqual(expected, actual)

    def test_heapsort_bigExample(self):
        arr = self.get_values(400)
        actual = dac.heapsort(arr)
        expected = sorted(arr)
        self.assertEqual(expected, actual)

    def test_maxHeapIncrement_SingleIncreasesKey(self):
        arr = [0, 2]
        expected = [0, 4]
        dac.maxHeapIncrement(arr, 1, 4)
        self.assertEqual(expected, arr)

    def test_maxHeapIncrement_SwapsTwo(self):
        arr = [0, 2, 1]
        expected = [0, 8, 2]
        dac.maxHeapIncrement(arr, 2, 8)
        self.assertEqual(expected, arr)

    def test_maxHeapIncrement_ValueNotLarger_RaisesException(self):
        arr = [0, 2, 1]
        self.assertRaises(Exception, dac.maxHeapIncrement, arr, 2, 0)

    def test_maxHeapAdd_Empty_SetsAsRoot(self):
        arr = [0]
        expected = [0, 1]
        dac.maxHeapAdd(arr, 1)
        self.assertEqual(expected, arr)

    def test_maxHeapAdd_BiggestElement_BecomesRoot(self):
        arr = [0, 4, 3, 2, 1]
        dac.maxHeapAdd(arr, 17)
        root = arr[1]
        self.assertEqual(17, root)

    def test_maxHeapExtractMax_returnsMaxValidHeapRemains(self):
        values = self.get_values(400)
        values[0] = 0
        maxvalue = max(values)
        dac.build_maxHeap(values)
        maxActual = dac.maxHeapExtractMax(values)
        self.assertEqual(maxvalue, maxActual)

    def get_values(self, size):
        return [random.randint(1, 10000000) for _ in range(size)]


if __name__ == '__main__':
    unittest.main()
