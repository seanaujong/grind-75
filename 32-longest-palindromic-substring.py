"""
https://leetcode.com/problems/longest-palindromic-substring/

Topics: String, Dynamic Programming
"""

"""
https://leetcode.com/problems/longest-palindromic-substring/discuss/2954/Python-easy-to-understand-solution-with-comments-(from-middle-to-two-ends)

At each character, expand twice, one for assuming
odd case, and one for assuming even case. Keep track
of the longest palindrome overall.
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer = ""
        for i in range(len(s)):
            answer = max(
                self.expand(s,i,i), # odd case
                self.expand(s,i,i+1), # even case
                answer,
                key=len)
        return answer
    
    def expand(self, s, l, r):
        while 0<=l and r<len(s) and s[l]==s[r]:
            l -= 1
            r += 1
        # s[l] != s[r] at the end of the loop
        # therefore take the PREVIOUS slice
        return s[l+1:r]
