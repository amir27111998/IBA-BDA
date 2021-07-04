# select one element
# compare the whole array with this element


arr = [1, 3, 3, 2, 4, 1, 5, 2, 4, 7, 2, 8]
for i in range(len(arr)):
    minInd = i
    for k in range(i, len(arr)):
        if arr[minInd] > arr[k]:
            minInd = k
    temp = arr[minInd]
    arr[minInd] = arr[i]
    arr[i] = temp

print(arr)
