#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def reverse(x: int) -> int:
        if x < 0:
            ans = int("-" + str(abs(x))[::-1])
        else:
            ans = int(str(abs(x))[::-1])
        return ans
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif Solution.reverse(x) == x:
            return True
        return False
# @lc code=end

