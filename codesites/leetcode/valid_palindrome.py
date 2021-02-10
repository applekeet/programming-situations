# valid palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        alp = ""
        for x in s:
            if x.isalpha():
                alp += x
        s1 = alp.lower()
        print(s1)
        return s1[::-1] == s1
        
s = Solution()

print(s.isPalindrome("0P"))
