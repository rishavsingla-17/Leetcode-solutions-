# this is a problem of binary search in this two different binary search applies one is to calculate first and one is to calculate 
# last in the code first and end was intialised by -1 in case of element is not find so they return -1 but if found in case of first
# binary seach if mid == target pehle us mid ko first me store krwado as array has duplcated also to binary search continue hoga to 
# check ki isse pehle bhi to ye element present nhi hai and 2nd binary search me bhi yahi hai
class Solution(object):
    def searchRange(self, nums, target):
        n = len(nums)
        low = 0
        high = n-1
        first,end = -1,-1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                first = mid 
                high = mid -1
            elif target > nums[mid]:
                low = mid+1
            else:
                high = mid-1
        low,high = 0,n-1
        while low<=high:
            mid = (low+high)//2
            if nums[mid] == target:
                end = mid 
                low = mid + 1
            elif target > nums[mid]:
                low = mid+1
            else:
                high = mid-1
        if first == -1 and end == -1:
            return[-1,-1]
        return[first,end]
