def left_rotate(arr, k):
    n = len(arr)
    k = k % n

    arr[:] = arr[k:] + arr[:k]


def right_rotate(arr, k):
    n = len(arr)
    k = k % n

    arr[:] = arr[-k:] + arr[:-k]


# Example
arr = [1, 2, 3, 4, 5, 6, 7]

left_rotate(arr, 2)
print("Left rotation:", arr)

right_rotate(arr, 2)
print("Right rotation:", arr)