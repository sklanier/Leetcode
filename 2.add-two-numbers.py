#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur1, cur2 = l1, l2
        while cur1 and cur2:
            print(cur1.val, cur2.val)
            cur1, cur2 = cur1.next, cur2.next
Solution.addTwoNumbers(ListNode(2), ListNode(5))
# @lc code=end

