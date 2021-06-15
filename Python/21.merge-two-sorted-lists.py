#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = None
        cur1 = l1
        cur2 = l2
        while cur1 and cur2:
            if cur1.value <= cur2.value:
                l3

    def push(self, value):
        new_node = ListNode(value)
        new_node.next = self.head
        self.head = new_node

Solution.mergeTwoLists([1,2,4])
# @lc code=end

