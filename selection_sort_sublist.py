def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j][0] < arr[min_index][0]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

arr = [[3, 5], [1, 2], [4, 6], [2, 1]]
selection_sort(arr)
print("Hasil pengurutan:", arr)