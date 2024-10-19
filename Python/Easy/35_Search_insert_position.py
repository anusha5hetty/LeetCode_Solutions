# https://leetcode.com/problems/search-insert-position/
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for (idx, num) in enumerate(nums):
            if num == target or num>target:
                return idx
        return len(nums)
    
    def searchInsertOtherSoln(self, nums: List[int], target: int) -> int:
        # The below solution works with O(log n) because 2 pointers are used.
        left = 0 
        right = len(nums) - 1

        while left <= right:
            middle = left + (right - left) // 2

            if nums[middle] == target:
                return middle
            if nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
        
        return left


nums = [1,3,6,8]
target = 2
print(Solution().searchInsert(nums, target))