# https://leetcode.com/problems/remove-element/description/

from typing import List

class Solution:
    def removeElementMySoln(self, nums: List[int], val: int) -> int:
        len_nums = len(nums)
        idx = 0
        processed = 0
        while processed < len_nums:
            if nums[idx] == val:
                nums.pop(idx)
            else:
                idx += 1
            processed +=1
        return idx
    
    def removeElementBetterSoln(self, nums: List[int], val: int) -> int:
        k = 0

        for num in nums:
            if num != val:
                nums[k] = num
                k = k+1
        return k