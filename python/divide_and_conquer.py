def find_max_crossing_subarray(A, low, mid, high):
    left_sum = -float("inf")
    sum = 0
    for i in range(mid, low - 1, -1):
        sum = sum + A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    right_sum = -float("inf")
    sum = 0
    for j in range(mid+1, high+1):
        sum = sum + A[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
    return (max_left, max_right, left_sum + right_sum)


def find_max_subarray(A, low, high):
    if high == low:
        # base case with single element
        return (low, high, A[low])
    mid = (low + high) // 2
    (left_low, left_high, left_sum) = find_max_subarray(A, low, mid)
    (right_low, right_high, right_sum) = find_max_subarray(A, mid + 1, high)
    (cross_low, cross_high, cross_sum) = find_max_crossing_subarray(
        A, low, mid, high)

    # decision tree
    if left_sum >= right_sum and left_sum >= cross_sum:
        return (left_low, left_high, left_sum)
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return (right_low, right_high, right_sum)
    else:
        return (cross_low, cross_high, cross_sum)


def brute_maxsubarray(A):
    size = len(A)
    max_sum = A[0]
    right_index = left_index = 0
    for i in range(size - 1):
        sum = A[i]
        if sum > max_sum:
                left_index = i
                right_index = i
                max_sum = sum
        for j in range(i + 1, size):
            sum += A[j]
            if sum > max_sum:
                left_index = i
                right_index = j
                max_sum = sum
    if A[size - 1] > max_sum:
        left_index = right_index = size - 1
        max_sum = A[size - 1]
    return (left_index, right_index, max_sum)


def linear_maxsubarray(A):
    max_sum = sum = A[0]
    left_marker = right_marker = 0
    max_details = (left_marker, right_marker, max_sum)
    for current in range(1, len(A)):
        # positive, so add it to sum
        if A[current] > 0:
            right_marker = current
            if sum > 0:
                sum += A[current]
            else:
                # don't hold onto the negative past
                sum = A[current]
                # mark our new extent
                left_marker = current
        # negative numbers here
        # would take our array negative, so the ride ends here
        elif sum + A[current] < 0:
            sum = A[current]
            right_marker = left_marker = current
        # add it to sum as as sum is still positive
        else:
            right_marker = current
            sum += A[current]
        if sum > max_sum:
            max_sum = sum
            right_marker = current
            max_details = (left_marker, right_marker, max_sum)
    return max_details


def max_heapify(A, index):
    l = 2 * index
    r = 2 * index + 1
    heap_size = len(A)
    if l < heap_size and A[l] > A[index]:
        largest = l
    else:
        largest = index
    if r < heap_size and A[r] > A[largest]:
        largest = r
    if largest != index:
        A[index], A[largest] = A[largest], A[index]
        max_heapify(A, largest)


def maxHeapIncrement(A, index, key):
    if key < A[index]:
        raise Exception('new key is smalley than current key')
    A[index] = key
    while index > 1 and A[index // 2] < A[index]:
        A[index], A[index // 2] = A[index // 2], A[index]
        index = index // 2


def maxHeapExtractMax(A):
    if len(A) == 1:
        raise Exception('heap underflow')
    max = A[1]
    A[1] = A[len(A) - 1]
    max_heapify(A, 1)
    return max


def maxHeapAdd(A, key):
    A.append(key)
    maxHeapIncrement(A, len(A) - 1, key)


def min_heapify(A, index):
    l = 2 * index
    r = 2 * index + 1
    heap_size = len(A)
    if l < heap_size and A[l] < A[index]:
        smallest = l
    else:
        smallest = index
    if r < heap_size and A[r] < A[smallest]:
        smallest = r
    if smallest != index:
        A[index], A[smallest] = A[smallest], A[index]
        min_heapify(A, smallest)


def build_maxHeap(A):
    heap_size = len(A)
    midpoint = heap_size // 2
    for index in range(midpoint, 0, -1):
        max_heapify(A, index)


def heapsort(A):
    # starts with 0 [0, max, 4, 2, ...]
    unsorted = A
    if unsorted[0] != 0:
        unsorted = [0] + unsorted
    build_maxHeap(unsorted)
    sorted = []
    while len(unsorted) > 2:
        sorted.append(unsorted[1])
        unsorted[1] = unsorted.pop()
        max_heapify(unsorted, 1)
    sorted.append(unsorted.pop())
    # get rid of the 0
    return sorted[::-1]
