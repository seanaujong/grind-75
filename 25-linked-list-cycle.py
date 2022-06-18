"""
https://leetcode.com/problems/linked-list-cycle/

Topics: Linked List, Fast/Slow Pointers

https://leetcode.com/problems/linked-list-cycle/discuss/1829489/C%2B%2B-oror-Easy-To-Understand-oror-2-Pointer-oror-Fast-and-Slow
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow: return True
        return False
        