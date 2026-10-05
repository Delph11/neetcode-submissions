class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {} # create a dictionary o store the items
        
        char_cnt = [] # create a 26 length array
        for i in range(0,26):
            char_cnt.append(0)

        for item in strs: # take an string from the strs
            for char in item: #take a alphabet from the string
                asc_cd = ord(char) # find its ascii code
                if asc_cd in range(65,91): # using the ascii code inc or dec the counter in the array
                    index = asc_cd-65
                    char_cnt[index] +=1
                if asc_cd in range(97,123): # using the ascii code inc or dec the counter in the array
                    index = asc_cd-97
                    char_cnt[index] +=1
            key = tuple(char_cnt) # add the array now as a key by converting into a tuple as key needs to be immutable, in the dictionary
            if key not in d:
                d[key] = []
                d.get(key).append(item)
            else:
                d.get(key).append(item)
            for j in range(0,26):
                char_cnt[j] = 0


        op = [] # now one by one we have to take all the lists from the dictionary in the values and add it to the master output list
        for key in d:
            op.append(d.get(key,[]))
        return op