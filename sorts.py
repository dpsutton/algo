import random
import math


def insertion_sort(values):
    sorting = list(values)
    for index in range(1, len(sorting)):
        key = sorting[index]
        j = index - 1
        while j >= 0 and sorting[j] > key:
            sorting[j + 1] = sorting[j]
            j -= 1
        sorting[j + 1] = key
    return sorting


def merge(A, left, middle, right):
    """
     A is the array, p the first index, q the second index and r the
    end.
    """
    leftSubArray = A[left:middle]
    rightSubArray = A[middle:right+1]
    leftSubArray.append(float("inf"))
    rightSubArray.append(float("inf"))
    i = j = 0
    for k in xrange(left, right + 1):
        if leftSubArray[i] < rightSubArray[j]:
            A[k] = leftSubArray[i]
            i += 1
        else:
            A[k] = rightSubArray[j]
            j += 1
    return A


def merge_sort(A, start, end):
    if start < end:
        middle = (start + end) // 2
        merge_sort(A, start, middle)
        merge_sort(A, middle + 1, end)
        merge(A, start, middle + 1, end)
    return A


def get_values(size):
    return [random.randint(1, 1000000) for _ in range(size)]
