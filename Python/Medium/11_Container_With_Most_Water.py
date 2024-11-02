# https://leetcode.com/problems/container-with-most-water/
from typing import  List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        first_idx = 0
        last_idx = len(height)-1
        most_water = 0

        while first_idx<last_idx:
            gap = last_idx - first_idx

            if height[last_idx] < height[first_idx]:
                water =  gap * height[last_idx]
                last_idx -= 1
            else:
                water = gap * height[first_idx]
                first_idx += 1

            if most_water<water:
                most_water = water

        return most_water

print(Solution().maxArea([1,1]))
