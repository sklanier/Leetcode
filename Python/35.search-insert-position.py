#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        elif len(nums) < 2:
            if target < nums[0]:
                return 0
            else:
                return 1
        else:
            for i in range(len(nums) - 1):
                if target > nums[i] and target < nums[i + 1]:
                    return i + 1
                elif target > nums[-1]:
                    return len(nums)
                elif target < nums[0]:
                    return 0
                else:
                    continue
# @lc code=end

