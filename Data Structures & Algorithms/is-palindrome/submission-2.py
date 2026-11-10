class Solution:
    def isPalindrome(self,s):
        lo = 0
        hi = len(s)-1

        while lo<=hi:
            while lo<hi and not(self.isalphanum(s[lo])):
                lo += 1
            while hi>lo and not(self.isalphanum(s[hi])):
                hi -= 1
            if (s[lo].lower()!=s[hi].lower()):
                return False
            lo += 1
            hi -= 1
        return True

    def isalphanum(self,c):
        return (ord('A')<=ord(c)<=ord('Z') or
                ord('a')<=ord(c)<=ord('z') or
                ord('0')<=ord(c)<=ord('9'))