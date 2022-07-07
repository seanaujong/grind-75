"""
https://leetcode.com/problems/min-stack/

Topics: Stack, Design

https://leetcode.com/problems/min-stack/discuss/49022/My-Python-solution
"""

class MinStack:

    def __init__(self):
        # keep track of both val AND the min so far
        # start off with a sentinel
        self.stack = [(-1, float('inf'))]

    def push(self, val: int) -> None:
        # the min is either the min so far, or the new val
        self.stack.append([val, min(val, self.stack[-1][1])])

    def pop(self) -> None:
        # if len(self.stack) <= 1: return
        self.stack.pop()

    def top(self) -> int:
        # if len(self.stack) == 1: return None
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
