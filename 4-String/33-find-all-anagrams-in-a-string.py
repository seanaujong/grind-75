"""
https://leetcode.com/problems/find-all-anagrams-in-a-string/

Topics: Sliding Window

https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/92007/Sliding-Window-algorithm-template-to-solve-all-the-Leetcode-substring-search-problem.
"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = list()
        # build hashmap
        stillNeed = dict()
        for c in p:
            if c not in stillNeed:
                stillNeed[c] = 0
            stillNeed[c] += 1
        # sliding window
        left = 0
        right = 0
        uniqueLetters = len(stillNeed)
        
        while right < len(s):
            # expand
            rc = s[right]
            if rc in stillNeed:
                stillNeed[rc] -= 1
                if stillNeed[rc] == 0:
                    uniqueLetters -= 1
            right += 1
            # reclaim
            while uniqueLetters == 0:
                # all entries in dict are 0
                lc = s[left]
                if lc in stillNeed:
                    stillNeed[lc] += 1
                    if stillNeed[lc] >= 1:
                        uniqueLetters += 1
                if right - left == len(p):
                    result.append(left)
                left += 1
            
        return result
        
