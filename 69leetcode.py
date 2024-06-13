import math


def binary(start, end, arr):
    newmid = 0
    while (start <= end):

        mid = start + (end - start) // 2
        if (mid * mid <= arr):
            start = mid + 1
            newmid = mid
        else:
            end = mid
    return newmid


def tar(arr):
    extrastart = arr - 1
    start = arr
    end = 0

    c = math.sqrt(arr)

    if (c == None):
        while (start <= end):
            if (arr == 0 or arr == 1):
                return 0

            mid = start + (end - start) // 2
            if (mid < arr):
                f = binary(mid + 1, end, arr)
                if (f == -1):
                    d = binary(start, mid, arr)
                    return d
                else:
                    return f
    return int(c)


d = tar(2147395599)
print(d)