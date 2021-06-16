#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)-1,-1,-1):
            if nums[i-1] == val:
                del nums[i-1]
        
# @lc code=end

