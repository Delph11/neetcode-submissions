class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        running_prod = 1
        prefix = []
        for i in range(0,n):
            prefix.append(running_prod)
            running_prod *= nums[i]
        running_prod = 1
        suffix = []
        for j in range(-1,-(n+1),-1):
            suffix.append(running_prod)
            running_prod *= nums[j]
        res = []
        for i in range(0,n):
            res.append(prefix[i]*suffix[-1-i])
        return res
