# Binary Search
# Finding an element in a sorted array by cutting in half
# O(logn)


# Iterative
def binarySearch(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1

    return -1


arr = [3, 4, 5, 6, 7, 8, 9]
x = 5
print(binarySearch(arr, x), "Iterative")

# Recursive
def binarySearch2(arr, x, low, high):
    if low <= high:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch2(arr, x, low, mid - 1)
        elif arr[mid] < x:
            return binarySearch2(arr, x, mid + 1, high)
    else:
        return -1

print(binarySearch2(arr, x, 0, len(arr) - 1), "Recursive")
