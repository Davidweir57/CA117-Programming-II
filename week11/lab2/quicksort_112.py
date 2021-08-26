def partition(A, p, r):

    # q and j start at p
    q = j = p

    # up to but not including pivot
    while j < r:

        # move values less than or equal to pivot and update q
        if A[j] <= A[r]:
            A[q], A[j] = A[j], A[q]
            q += 1

        j += 1

    # swap pivot with A[q]
    A[q], A[r] = A[r], A[q]

    # return pivot index
    return q

# recursively partition list until sorted
def quicksort(A, p, r):

    # return if nothing to sort (zero or one element)
    if r <= p:
        return

    # partition and sort left and right sublists
    q = partition(A, p, r)
    quicksort(A, p, q - 1)
    quicksort(A, q + 1, r)
