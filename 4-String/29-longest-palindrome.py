"""
https://leetcode.com/problems/longest-palindrome/

Topics: String, Set

The length of the longest palindrome is the
length of the string minus the number of
unpaired characters, although we can put
one unpaired character in the middle.
"""

class Solution:
    def longestPalindrome(self, s: str) -> int:
        cache = set()
        for c in s:
            if c in cache:
                cache.remove(c)
            else:
                cache.add(c)
        if cache:
            # len(cache) is the count of unpaired character
            # + 1 because we can put one odd character in the middle
            return len(s) - (len(cache) + 1)
        else:
            # obviously we cannot + 1 if we don't have an unpaired
            return len(s)
        
