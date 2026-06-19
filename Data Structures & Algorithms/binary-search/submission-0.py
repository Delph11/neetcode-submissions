class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)-1
        lo = 0
        hi = n

        while(lo<=hi):
            mid = (lo+hi)//2
            if nums[mid]<target:
                lo = mid+1
            elif nums[mid]>target:
                hi = mid-1
            else :
                return mid
        
        return -1
        