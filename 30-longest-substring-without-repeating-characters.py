"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Topics: Sliding Window

Keep two pointers (a sliding window) which define the max substring.
In our case, this is start and i.
Keep a hashmap which stores at which position we have
last seen each character to check for repeats.
When we see a repeat, move the start pointer to the right of it.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        longest = 0
        used = dict()
        for i, c in enumerate(s):
            if c in used and start <= used[c]:
                start = used[c] + 1
            else:
                longest = max(longest, i - start + 1)
            used[c] = i
        return longest
        
