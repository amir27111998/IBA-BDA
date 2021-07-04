# Pick 2 elements and compare them and swap them
# This requires 2 loops


arr = [1, 3, 3, 2, 4, 1, 5, 2, 4, 7, 2, 8]
for i in range(len(arr)):
    for j in range(len(arr)-1):
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
print(arr)