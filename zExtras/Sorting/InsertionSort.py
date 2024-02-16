# Insertion Sort
# O(n^2)
# We loop throught the array in the first iteration which will be our key
# And we check the left of a key with a while loop
# If key is smaller than the left of the key we move the left to right until key isnt smaller
# Than we set where we left of as key
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(arr, i)
    return arr



arr = [10, 5, 8, 2, 18, 25, 15, 1, 20, 4]
print(insertionSort(arr))