"""
https://leetcode.com/problems/first-bad-version/

Topics: Binary Search

https://leetcode.com/problems/first-bad-version/discuss/769685/Python-Clear-explanation-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems.
"""

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo = 1
        hi = n
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if isBadVersion(mid): hi = mid
            else: lo = mid + 1
		# doesn't apply in this problem because there is always a bad version
        if not isBadVersion(lo):
            return -1
        return lo
        
