def tar(arr):
    c = list(set(arr))
    if (len(c) == len(arr)):
        return False
    else:
        return True
c=tar([1,2,3,4])
print(c)





