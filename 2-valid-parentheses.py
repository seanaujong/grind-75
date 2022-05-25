"""
https://leetcode.com/problems/valid-parentheses/submissions/

Keywords: stack

O(N) one pass solution

- Put left-brackets on the stack
- When we hit a right-bracket, compare with the last seen left-bracket.
- We get the last seen left-bracket by popping it off the stack
"""

class Solution:
    def isValid(self, s: str) -> bool:
        # odd length strings are obviously invalid
        if len(s) % 2 == 1:
            return False
        
        stack = []
        mapping = {'(':')', '[':']', '{':'}'}
        for c in s:
            if c in mapping:
                # append left brackets
                stack.append(c)
            else:
                # pop the rightmost seen left bracket
                # check if it corresponds with the
                # current right bracket
                if not stack or mapping[stack.pop()] != c:
                    return False
        return not stack
        