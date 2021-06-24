#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root) -> int:
        if root is None:
            return 0
        
        leftDepth = Solution.maxDepth(self, root.left)
        rightDepth = Solution.maxDepth(self, root.right)

        if leftDepth > rightDepth:
            return leftDepth + 1
        return rightDepth + 1

        
# @lc code=end

