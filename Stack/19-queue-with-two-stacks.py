"""
https://leetcode.com/problems/implement-queue-using-stacks

Topics: Stack, Design, Queue

https://leetcode.com/problems/implement-queue-using-stacks/discuss/64198/Share-my-python-solution-(32ms)/179427

Play with this example to help explain why we shift only when s2 is empty:

1 2 3
-

Peek, then add 4, and go from there.

This optimization gives us O(1) push and O(1) amortized pop
"""

class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x):
        self.s1.append(x)

    def pop(self):
        self.peek()
        return self.s2.pop()

    def peek(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]        

    def empty(self):
        return not self.s1 and not self.s2
