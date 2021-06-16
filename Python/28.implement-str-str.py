#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < 1 or len(needle) < 1:
            if len(needle) > 0:
                return -1
            return 0
        if needle not in haystack:
            return -1
        return haystack.index(needle)
# @lc code=end

