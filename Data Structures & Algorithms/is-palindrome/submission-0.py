class Solution:
    def isPalindrome(self, s):
        lo = 0
        hi = len(s)-1
        while lo<=hi:
            ol = ord(s[lo])
            oh = ord(s[hi])
            if not((ol>=48 and ol<=57) or (ol>=65 and ol<=90) or (ol>=97 and ol<=122)):
                lo += 1
                continue
            if not((oh>=48 and oh<=57) or (oh>=65 and oh<=90) or (oh>=97 and oh<=122)):
                hi -= 1
                continue 
            if (s[lo].lower()==s[hi].lower()):
                lo += 1
                hi -= 1
            else:
                return False
        return True 