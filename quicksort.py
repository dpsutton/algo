import random as random


def quicksort(A, start, end):
    if start <= end:
        pivot = randomized_partition(A, start, end)
        quicksort(A, start, pivot - 1)
        quicksort(A, pivot + 1, end)


def tailRecursiveQuicksort(A, start, end):
    while start < end:
        pivot = randomized_partition(A, start, end)
        # first call recurses on first half
        tailRecursiveQuicksort(A, start, pivot - 1)
        # now set to work on the second half
        start = pivot + 1


def partition(A, start, end):
    pivot = A[end]
    i = start - 1
    for j in range(start, end):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    pivotPosition = i + 1
    A[pivotPosition], A[end] = A[end], A[pivotPosition]
    return pivotPosition


def randomized_partition(A, start, end):
    i = random.randint(start, end)
    A[i], A[end] = A[end], A[i]
    return partition(A, start, end)


def make_intervals(count):
    intervals = []
    for _ in range(count):
        start = random.randint(1, 40)
        end = start + 4
        intervals.append(Interval(start, end))
    return intervals


class Interval(object):
    """
    Interval contains a start point and an end point
    has properties: start:int end:int
    """

    def __init__(self, start, end):
        super(Interval, self).__init__()
        self.start = start
        self.end = end

    def length(self):
        return self.end - self.start

    def overlaps(self, i):
        if self.start < i.start:
            return self.end >= i.start
        return i.end >= self.start

    def containsPointBefore(self, i):
        return self.overlaps(i) or self.start < i.start


def fuzzyPartition(intervals, start, end):
    """ 
    Given a list of intervals, choose the last one and partition
    so that the intervals before the pivot contain a point before
    intervals following
    start: integer
    end: integer
    intervals: list of Intervals
    """
    pivot = intervals[end]
    i = start - 1
    for j in range(start, end):
        if intervals[j].containsPointBefore(pivot):
            i += 1
            intervals[i], intervals[j] = intervals[j], intervals[i]

    pivotPosition = i + 1
    intervals[pivotPosition], intervals[end] = \
        intervals[end], intervals[pivotPosition]
    return pivotPosition
