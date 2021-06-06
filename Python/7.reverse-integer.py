#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            ans = int("-" + str(abs(x))[::-1])
        else:
            ans = int(str(abs(x))[::-1])
        if abs(ans) > 2**31:
            return 0
        else:
            return ans
# @lc code=end

