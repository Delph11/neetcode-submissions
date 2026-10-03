class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_dict = {}
        for i in range(0,len(nums)):
            diff = target-nums[i]
            if diff not in diff_dict:
                    key = diff
                    value = i
                    diff_dict[key] = []
                    diff_dict[key].append(value)
            else:
                    diff_dict[key].append(value)
            if nums[i] in diff_dict:
                    if diff_dict.get(nums[i])[0] != i:
                        ans = [diff_dict.get(nums[i])[0],i]
                        ans.sort()
                        return ans
            else:
                    i+=1
            