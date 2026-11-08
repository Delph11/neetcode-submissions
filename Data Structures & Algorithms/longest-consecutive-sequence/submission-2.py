class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums) # converting to set removes duplicates and also just like dictioanry set gives O(1) search time. 
        longest = 0
        for item in nums :
            if (item-1) not in numsSet: # then this means the item is the start of a sequence as there is no immediate smaller number to it. If there was then it comes later in the sequence and not at the start.
                length = 0
                while (item + length) in numsSet: # eg. 2 + 0 = 2 in set, 2 + 1 = 3 True, 2 + 2 = 4, 2 + 3 = 5 True, 2 + 4 = 6 False so length = 4
                    length +=1
                longest = max (longest,length)
        return longest