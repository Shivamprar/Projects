class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums2length = len(nums2)
        totalneeded = m + n

        for i in range(0, nums2length ):
            nums1[m + i] = nums2[i]
        nums=nums1[:totalneeded]

        for j in range(0,len(nums)-1):
            for k in range(1,len(nums)-j):
                if(nums[k-1]>nums[k]):
                    nums[k-1],nums[k]=nums[k],nums[k-1]
        for z in range(0,len(nums1)):
            nums1[z]=0
            nums1[z]+=nums[z]
        print(nums1)