"""
https://leetcode.com/problems/valid-palindrome/

Topics: Two Pointers, String

The idea is to keep a left and right pointer. This lets us
"skip" non-alphanumeric characters without having to modify the string.
Loop until our pointers have converged (left crosses right).
During the interview, it would be good to point out that we need
to lowercase all the letters, and that the constraints involve
the string length being at least 1 (no zero case).
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointer solution
        left = 0
        right = len(s) - 1
        # while we haven't converged...
        while left < right:
            # "after converting all uppercase letters into lowercase letters"
            a = s[left].lower()
            b = s[right].lower()
            if not a.isalnum():
                # skip
                left += 1
            elif not b.isalnum():
                # skip
                right -= 1
            else:
                # compare
                if a != b:
                    return False
                left += 1
                right -= 1
        # converged successfully!
        return True
        
