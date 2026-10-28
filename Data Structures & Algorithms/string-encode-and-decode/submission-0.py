class Solution:
    def encode(self,strs):
        encoded_str = ""
        for item in strs:
            encoded_str += (str(len(item)) + "#" + item)
            
        return encoded_str
        
    def decode(self,s):
        decoded_str = []
        i = 0
        num = []
        while i<len(s):
            if s[i] != '#':
                num.append(s[i])
                i += 1
            else:
                count = int("".join(num))
                j = i
                res = ""
                while count>0 :
                    j += 1
                    res = res + s[j]
                    
                    count -= 1 
                decoded_str.append(res)
                
                i = j+1
                num = []
        return decoded_str