"""
https://leetcode.com/problems/minimum-window-substring/

Topics: Sliding Window

https://leetcode.com/problems/minimum-window-substring/discuss/26808/Here-is-a-10-line-template-that-can-solve-most-'substring'-problems

1. Sliding window with two pointers
2. Move end until we find a valid window
3. When a valid window is found, move start to find a smaller window
"""

from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        containing = defaultdict(int)
        start = 0
        end = 0
        count = len(t)
        minStart = 0
        minLen = float('inf')
        
        for c in t:
            containing[c] += 1
            
        while end < len(s):
            # expand
            curr = s[end]
            if curr in containing:
                if containing[curr] > 0:
                    count -= 1
                containing[curr] -= 1
            # shrink
            while count == 0:
                curl = s[start]
                if end - start + 1 < minLen:
                    minLen = end - start + 1
                    minStart = start
                if curl in containing:
                    containing[curl] += 1
                    if containing[curl] > 0:
                        count += 1
                start += 1
            end += 1
        
        if minLen < float('inf'):
            return s[minStart:minStart + minLen]
        else:
            return ""
