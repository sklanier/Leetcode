#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        while len(s) > 0:
            temp = s
            s = s.replace('()','')
            s = s.replace('[]','')
            s = s.replace('{}','')
            if temp == s:
                return False
        return True
        
# @lc code=end

