class Solution:
    def findMedianSortedArrays(self, arr: List[int], arr1: List[int]) -> float:
        c = arr + arr1
        c.sort()
        start = 0
        end = len(c) - 1
        while (start <= end):
            mid = start + (end - start) // 2
            if (len(c) < 2):
                return c[mid]

            if (len(c) % 2 == 0):
                d = c[mid] + c[mid + 1]
                total = d / 2
                return float(total)
            else:
                return c[mid]              
