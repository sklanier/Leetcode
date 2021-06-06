#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
import math

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insert(root, item):
        temp = ListNode(item)

        if (root == None):
            root = temp
        else:
            pointer = root
            while (pointer.next != None):
                pointer = pointer.next
            pointer.next = temp
        return root
    def arrayToList(arr , n):
        root = None
        for i in range(0, n, 1):
            root = Solution.insert(root, arr[i])
        return root
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur1, cur2 = l1, l2
        num1 = []
        num2 = []
        out1 = ''
        out2 = ''
        l3 = None
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
        final = []
        
        for i in range(len(out1)):
            final.append(int(out1[i])+int(out2[i]))
        for i in range(len(final)):
            if final[i] > 9:
                final[i] -= 10
                final[i+1] += 1

        print(final)
        n = len(final)
        l3 = Solution.arrayToList(final, n)
        return l3
 # @lc code=end

