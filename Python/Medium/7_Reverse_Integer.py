# https://leetcode.com/problems/reverse-integer/
import math

class Solution:
    def reverse(self, x: int) -> int:
        reversed_x = 0
        is_neg = x<0
        x = abs(x)
        while x != 0:
            
            reversed_x = (reversed_x * 10) + (x % 10)
            if reversed_x < math.pow(-2, 31) or reversed_x > math.pow(2, 31)-1:
                return 0
            
            x = x//10

        if is_neg:
            return -reversed_x
        return reversed_x
    
print(Solution().reverse(1534236469))