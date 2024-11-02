# https://leetcode.com/problems/two-sum/description/

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct_map = {}

        for idx, num in enumerate(nums):
            if(num in dct_map):
                return [dct_map[num], idx]
            
            dct_map[target-num] = idx
        return [-1, -1]


nums = [2,7,11,15]
print(Solution().twoSum(nums, 17))