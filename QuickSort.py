def partition(A, p, r):
    i = (p - 1)  # index of smaller element
    x = A[r]  # last element

    for j in range(p, r-1):

        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]


    A[i + 1], A[r] = A[r], A[i + 1]
    return (i + 1)



# Function to do Quick sort
def quickSort(A, p, r):
    if p < r:
        # q is partitioning index, A[p] is now
        # at right place
        q = partition(A, p, r)
        quickSort(A, p, q - 1)
        quickSort(A, q + 1, r)



A=[10, 7, 8, 9, 1, 5]
partition(A,0,5)
quickSort(A,0,5)
n = len(A)
quickSort(A,0,n-1)
print("Sorted Array is",A)

