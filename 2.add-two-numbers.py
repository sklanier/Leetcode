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
        num1 = []
        num2 = []
        out1 = ''
        out2 = ''
        answer = []
        while cur1:
            num1.append(cur1.val)
            cur1 = cur1.next
        while cur2:
            num2.append(cur2.val)
            cur2 = cur2.next
        for _ in num1:
            out1 += str(_)
        for _ in num2:
            out2 += str(_)
        print(out1)
        print(out2)
        final = str(int(out1) + int(out2))
        for _ in final:
            answer.append(int(_))
        return answer
# @lc code=end

