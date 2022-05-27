"""
https://leetcode.com/problems/valid-parentheses/submissions/

Topics: stack

O(N) one pass solution

- Put left-brackets on the stack
- When we hit a right-bracket, compare with the last seen left-bracket.
- We get the last seen left-bracket by popping it off the stack

Cases:

- More left brackets than right brackets
- More right brackets than left brackets
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
                # first, see if there are more right brackets than left brackets (empty stack)
                # then check if the brackets match
                if not stack or mapping[stack.pop()] != c:
                    return False
        # check if there are more left brackets than right brackets
        return not stack
        