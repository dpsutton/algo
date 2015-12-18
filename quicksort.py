def quicksort(A, start, end):
    if start <= end:
        pivot = partition(A, start, end)
        quicksort(A, start, pivot - 1)
        quicksort(A, pivot + 1, end)


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
