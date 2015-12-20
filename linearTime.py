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
