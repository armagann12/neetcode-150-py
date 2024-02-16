# Insertion Sort
# O(n^2)

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