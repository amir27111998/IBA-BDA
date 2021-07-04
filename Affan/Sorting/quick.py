arr = [3, 700,  3, 90, 90, 80, 5, 11, 70]


def swap(num1, num2):
    num1 = num1 + num2
    num2 = num1 - num2
    num1 = num1 - num2
    return num1, num2


def partition(low, high):
    pivot_index = low
    i = pivot_index + 1
    j = high - 1
    while i < j:
        while i<=j and arr[i] < arr[pivot_index]:
            i = i + 1
        while arr[j] > arr[pivot_index]:
            j = j - 1
        if i < j:
            arr[i], arr[j] = swap(arr[i], arr[j])
    arr[pivot_index], arr[j] = swap(arr[pivot_index], arr[j])
    return j


def quick_sort(low, high):
    partition_index = partition(low, high)
    left_part = partition_index
    right_part = high
    # left Part
    while low != left_part:
        left_part = partition(low, left_part)
    # right Part
    while right_part != partition_index+1:
        right_part = partition(partition_index+1, right_part)
    return arr


print(quick_sort(0, len(arr)))