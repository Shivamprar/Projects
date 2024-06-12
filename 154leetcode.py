def arrs(arr):
    start = 0
    end = len(arr) - 1
    while (start < end):
        mid = start + (end - start) // 2
        if (mid > start and arr[mid] < arr[mid - 1]):
            return arr[mid]
        if (arr[start] == arr[mid] and arr[mid] == arr[end]):
            start += 1
            end -= 1
        if (mid < end and arr[mid + 1] < arr[mid]):
            return arr[mid + 1]
        if (arr[start] >= arr[end] and arr[mid] > arr[end]):
            start = mid + 1
        else:
            end = mid
    return arr[end]
c=arrs([2,0,1,1,1])
print(c)