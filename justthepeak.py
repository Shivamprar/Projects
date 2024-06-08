def peak(arr):
    start=0
    end=len(arr)-1

    while (start < end):
        mid = start + (end - start) // 2

        if (mid > start and arr[mid] < arr[mid - 1]):
            end = mid - 1
        if (mid < end and arr[mid] > arr[mid + 1]):
            return mid
        if (arr[mid] < arr[start]):
            end = mid
        else:
            start = mid + 1
    return start

def binarysearch(arr,target,start,end):
    while (start <= end):
        mid = start + (end - start) // 2
        if (len(arr) <= 1):
            if (target == arr[mid]):
                return mid
            else:
                return -1
        if (target == arr[mid]):
            return mid
        if (target < arr[mid]):
            end = mid - 1
        else:
            start = mid + 1

    return -1
def ret(nums,target):
    c = peak( nums)
    # print(c)
    d = binarysearch( nums, target, 0, c)
    # print(d)

    if (d == -1):
        f = binarysearch( nums, target, c + 1, len(nums) - 1)
        # print(f)
        return f
    if (nums[d] == target):
        return d
    return d


c1=[1,3]

target=3
j=ret(c1,target)
print(j)

