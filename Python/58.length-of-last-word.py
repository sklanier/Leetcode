#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        split = s.split(' ')
        while '' in split:
            split.remove('')
        if split:
            print(split)
            if split[-1] == '':
                return len(split[-2])
            return len(split[-1])
        return 0
# @lc code=end

