# merge sort takes an array as an argument
def merge_sort(arr):
    # if the the array has 1 or less elements than it is already sorted
    if len(arr) <= 1:
        return
    # this splits the array in half and stores them i separated arrays
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    # splits each array up until theres is only one element per array
    merge_sort(left)
    merge_sort(right)
    
    # merge 2 will sort the 2 arrays into one array
    merge_two(left, right, arr)

 # merge two takes the 2 sorted arrays and the unsorted array as arguments
def merge_two(a,b, arr):

    len_a = len(a)
    len_b = len(b)
    # keeps track of the indexes of each array
    i = j = k = 0

    # run this until the end of each loop
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1

    while i < len_a:
        arr[k] = a[i]
        i += 1
        k += 1
    while j < len_b:
        arr[k] = b[j]
        j += 1
        k += 1

arr = [30,55,3,43,123,88,92,600,95,2,37]

merge_sort(arr)
print(arr)
