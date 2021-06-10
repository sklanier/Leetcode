#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        count = 0
        print(strs[0])
        # 
        for i in range(len(strs)):
            for j in range(len(strs[i])+1):
                print(strs[i][:j])
        

# @lc code=end

