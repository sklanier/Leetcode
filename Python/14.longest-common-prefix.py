#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
import os
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # lcp = ''
        # if not strs: return lcp
        # shortest_str = min(strs, key=len)
        # for i in range(len(shortest_str)):
        #     if all([x.startswith(shortest_str[:i+1]) for x in strs]):
        #         lcp = shortest_str[:i+1]
        #     else:
        #         break
        # return lcp
        return os.path.commonprefix(strs)
# @lc code=end
