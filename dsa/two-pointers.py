# Consider the arr is sorted
def two_pointers(arr, target):
    left, right = 0, len(arr) - 1

    while left < right:
        result = arr[left] + arr[right]

        if (result == target):
            return True
        if (result < target):
            left += 1
        else:
            right -= 1

    return False


arr = [3, 4, 5, 6]
t = 5
print(two_pointers(arr, t))