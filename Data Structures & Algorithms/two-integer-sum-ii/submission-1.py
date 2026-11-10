class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo = 0
        hi = len(numbers)-1
        while lo<=len(numbers)-1 and hi>=0:
            sum = numbers[lo]+numbers[hi]
            if sum > target:
                hi -= 1
            elif sum < target:
                lo += 1
            elif sum == target:
                if lo == hi:
                    return []
                else:
                    if lo<hi:
                        return [lo+1,hi+1]
                    else:
                        return [hi+1,lo+1]