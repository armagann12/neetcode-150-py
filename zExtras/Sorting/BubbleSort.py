# Bubble Sort
# O(n^2)
# Max to end
# With every outer loop the biggest element will be at the end of array
# With every inner loop it will swap if its smaller/bigger or not
def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                tmp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = tmp
    return arr

arr = [10, 5, 8, 2, 18, 25, 15, 1, 20, 4]
print(bubbleSort(arr))

# Optimized version
def bubbleSort2(arr):
    for i in range(len(arr)):
        isSwapped = False
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                tmp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = tmp
                isSwapped = True
        if not isSwapped:
            break
    return arr

print(bubbleSort2(arr))