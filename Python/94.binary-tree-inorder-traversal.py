#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        cur = root
        output = []
        stack = []
        stack.append(root)
        while stack:

            if cur is None:
                cur = stack.pop()
                output.append(cur.val)
                cur = cur.right
            else:
                stack.append(cur)
                cur = cur.left
            print(stack, output)
        output.pop()
        return output
        
# @lc code=end

