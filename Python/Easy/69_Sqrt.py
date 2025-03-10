# https://leetcode.com/problems/sqrtx/description/
import math


class Solution:
    def mySqrtSimple(self, x: int) -> int:
        return math.floor(math.sqrt(x))
    
    def mySqrtActual(self, x: int) -> int:
        # using binary search
        if x == 0 or x == 1:
            return x
        start = 1
        end = x//2
        midIndex = end//2

        # midIndex**2 calculates the power of 2
        while start <= end and midIndex**2 != x:
            if midIndex**2 > x:
                end = midIndex - 1
            else:
                start = midIndex + 1
            midIndex = (start + end)//2
        return midIndex

Solution().mySqrtActual(81)