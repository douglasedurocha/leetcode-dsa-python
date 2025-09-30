# Consider the arr is sorted
def two_pointers(arr, target):
    lo, hi = 0, len(arr) - 1

    while lo < hi:
        result = arr[lo] + arr[hi]

        if (result == target):
            return True
        if (result < target):
            lo += 1
        else:
            hi -= 1

    return False


arr = [3, 4, 5, 6]
t = 9
print(two_pointers(arr, t))