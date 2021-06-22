#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        output = []
        num = ''
        for digit in digits:
            num += str(digit)
        plus_one = int(num) + 1
        for _ in str(plus_one):
            output.append(_)
        return output
# @lc code=end

