#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # O(n^2) SOLUTION TIMES OUT

        # if len(nums) < 2:
        #     return nums[0]
        
        # sub_lists = []
        # for i in range(len(nums) + 1):
        #     for j in range(i):
        #         sub_lists.append(nums[j: i])

        # print(sub_lists)

        # max_sum = sum(sub_lists[0])

        # for sub in sub_lists:
        #     if sum(sub) >= max_sum:
        #         max_sum = sum(sub)

        # return max_sum

        # O(n) "Kadane's" Algorithm
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)
# @lc code=end

