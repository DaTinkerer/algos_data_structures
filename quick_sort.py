# quick sort will take an array as an argument
def quicksort(arr):
    # quick sort will call another fucntion called qs.
    # qs takes the array, the first index of the array, and the last index of the array as arguments.
    # Basically it will run qs from the beginning to the end of the array
    qs(arr, 0, len(arr) - 1)

# in qs l is the first index and r is the last index of the array
# It runs qs from l to r
def qs(arr, l, r):
    # if l is greater than or equal to r then there is nothing to sort
    if l >= r:
        return
    # If it continues, qs will call the partition function and store the return value in p
    # this is the new index for pivot
    p = partition(arr, l, r)

    # runs qs on smaller unsorted parts of the array
    # now from the start to the index before the new pivot
    qs(arr, l, p - 1)
    # and from the index after the new pivot to the end
    qs(arr, p + 1, r)

# partition takes in l and r (the start and end of the array) as arguments
def partition(arr, l, r):
    # sets pivot as r
    pivot = arr[r]
    # sets i  as the index behind l or behind the start
    i = l - 1
    # for the index from l to r not including r
    for j in range(l, r):
        # if the index in the array is less than pivot
        # increment i and then swap the current j with the current i
        # if it's greater, do nothing
        # this will happen until the end of the loop
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    # after the loop, it sets a new pivot index
    return i + 1

a1 = [3, 2, 1]
a2 = [1, 2, 3]
a3 = []
a4 = [3, 1, -1, 0, 2, 5]
a5 = [2, 2, 1, 1, 0, 0, 4, 4, 2, 2, 2]
a6 = [0]
a7 = [3, -2, -1, 0, 2, 4, 1]
a8 = [1, 2, 3, 4, 5, 6, 7]
a9 = [2, 2, 2, 2, 2, 2, 2]

# quicksort(a1)
# quicksort(a2)
# quicksort(a3)
# quicksort(a4)
quicksort(a4)
print(a4)
# quicksort(a6)
# quicksort(a7)
# quicksort(a8)
# quicksort(a9)