from typing import List
#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        output = []
        for num in nums:
            if num not in output:
                output.append(num)
        return output
# @lc code=end

Solution.removeDuplicates("self", [1,3,4,5,6,6])