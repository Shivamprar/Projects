# def search(arr,target):
#     peak=peakindex(arr)
#     firsttry=orderagnoasticbinarysearch(arr,target,0,peak)
#     if(firsttry !=-1):
#         return firsttry
#     return orderagnoasticbinarysearch(arr,target,peak+1,len(arr)-1)
#
# def peakindex(arr):
#     start=0
#     end=len(arr)-1
#     while(start<end):
#         mid=start+(end-start)//2
#         if(arr[mid]>arr[mid+1]):
#             end=mid
#         else:
#             start=mid+1
#     return start
#
# def orderagnoasticbinarysearch(arr,target,start,end):
#     isasc=arr[start]<arr[end]
#     while(start<=end):
#         mid=start+(end-start)//2
#         if(arr[mid]==target):
#             return mid
#         if(isasc):
#             if((target)<arr[mid]):
#                 end=mid-1
#             else:
#                 start=mid+1
#         else:
#             if(target<arr[mid]):
#                 start=mid+1
#             else:
#                 end=mid-1
#     return -1




class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n=mountain_arr.length()
        low=0
        high=n-1
        max_index=0
        while low<high:
            mid=low+(high-low)//2
            if mountain_arr.get(mid)>mountain_arr.get(mid+1):
                high=mid
            else:
                low=mid+1
        max_index=low
        low=0
        high=max_index

        while low<=high:
            mid=low+(high-low)//2
            midarr=mountain_arr.get(mid)
            if midarr<target:
                low=mid+1
            elif midarr>target:
                high=mid-1
            else:
                return mid

        low=max_index
        high=n-1
        while low<=high:
            mid=low+(high-low)//2
            midarr=mountain_arr.get(mid)
            if midarr>target:
                low=mid+1
            elif midarr<target:
                high=mid-1

            else:
                return mid
        return -1