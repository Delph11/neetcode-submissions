class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i in nums:
            if i in d:
                d[i] = d.get(i) + 1
            else:
                d[i] = 1

        for k in d:
            if d.get(k)>1:
                return True
        return False