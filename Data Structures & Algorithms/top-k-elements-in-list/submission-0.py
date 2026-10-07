class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for item in nums:
            if item not in dict:
                dict[item] = 1
            else:
                dict[item] += 1
        arr = [float('-inf')] * k
        arr_key = ['a']*k
        for key in dict:
                item = dict.get(key)
            # print(f"\n key = {key} and item = {item} " )
            # if item not in arr: # not needed as we can have multiple numbers with the same frequency of occuring
                for i in range(0,k): 
                    if item > arr[i]:
                        #push arr items to right
                        j = -1
                        while j > (-k+i):
                            arr[j] = arr[j-1]
                            arr_key[j] = arr_key[j-1]   
                            j -= 1
                        arr[i] = item
                        arr_key[i] = key
                        break
        return [x for x in arr_key if x != 'a']

        