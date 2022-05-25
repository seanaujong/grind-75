"""
https://leetcode.com/problems/merge-two-sorted-lists/submissions/

Keywords: linked list, sentinel node

O(N) one-pass solution

https://leetcode.com/problems/merge-two-sorted-lists/discuss/759870/Python3-Solution-with-a-Detailed-Explanation-dummy-explained

- Keep a reference to the sentinel node at the beginning

- Remember to tack the remaining list onto the end of our result

Alternate solutions:

1. recursively

2. modify and return list1, inserting list2 into list1
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = ListNode()
        sentinel = cur
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        cur.next = list1 or list2
        return sentinel.next
            
        