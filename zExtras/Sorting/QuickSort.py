# Quick Sort
# O(nlogn)

# In partition there there is an array and we use from l to r
# Than we take far right as pivot and we loop throught the array from l to r
# Meanwhile we keep track of a pointer from the start so when we traverse the array and if the index of the elenent is smaller than pivot
# We swap the value from the index and the pointer and also increase our pointer
# Than at the end we swap the pivot with the pointer
# This way from pointers left side its smaller than pointer and right side is bigger thn pointer
def partition(array, l, r):
    pivot = array[r]
    pointer = l - 1
    print("l:", l, "r:",r)
    for j in range(l, r):
        if array[j] <= pivot:
            pointer += 1
            tmp = array[pointer]
            array[pointer] = array[j]
            array[j] = tmp
    array[r] = array[pointer + 1]
    array[pointer + 1] = pivot

    print("arr: ", array, "  pivot:", pointer + 1)

    return pointer + 1

# Than we do this util l<r using recursion
# We call quicksort from l to pivot - 1 and right to pivot - 1
# And than it becmose sorted
def quickSort(array, l, r):
    if l < r:
        pivot = partition(array, l, r)

        # recursive call on the left of pivot
        quickSort(array, l, pivot - 1)

        # recursive call on the right of pivot
        quickSort(array, pivot + 1, r)


data = [8, 7, 2, 1, 0, 9, 6]
print("Unsorted Array: ", data)

quickSort(data, 0, len(data) - 1)

print('Sorted Array: ', data)
