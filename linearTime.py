def countingSort(A, k):
    # A is the input

    # k is the size limit max of the input
    B = []
    C = [0] * (k + 1)
    for a in A:
        C[a] += 1
    for index in range(len(C)):
        for quantity in range(C[index]):
            B.append(index)
    return B


def stableCountingSort(A, k):
    C = [0 for _ in A]
    B = [0] * len(A)
    for value in A:
        C[value] += 1
    for i in range(1, k + 1):
        C[i] += C[i - 1]

    return B
