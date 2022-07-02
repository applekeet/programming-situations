## https://leetcode.com/problems/word-break/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        s_length = len(s)
        
        dp = [False] * (s_length + 1)
        dp[s_length]=True
        for i in range(s_length - 1, -1, -1):
            for word in wordDict:
                if (i + len(word)) <= len(s) and s[i:i+len(word)] == word:
                    dp[i] = dp[i + len(word)]
                if dp[i]:
                    break
            # print(i, word, dp)
        return dp[0]

'''

solution looks simple at first glance, however there is some intrinsic stuff going on.

leetcode - [leet, code]
i           8 7 6 5 4 3 2 1 0
len(word)   4 4 4 4 4 4 4 4
len(s)      8 8 8 8 8 8 8 8

So, comparing length and then checking the word itself the condition for true/false.


'''
        