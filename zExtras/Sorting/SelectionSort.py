# Selection Sort
# O(n^2)
# Min to begining
# Each iteration smallest value is set at the beggining of the array
def selectionSort(arr):
    for i in range(len(arr)):
        minIndex = i
        for j in range(i, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        tmp = arr[i]
        arr[i] = arr[minIndex]
        arr[minIndex] = tmp
    return arr



arr = [10, 5, 8, 2, 18, 25, 15, 1, 20, 4]
print(selectionSort(arr))