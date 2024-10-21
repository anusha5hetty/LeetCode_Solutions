#  https://leetcode.com/problems/plus-one/

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_digits = ''.join(map(str, digits))
        int_digits = int(str_digits) + 1
        return list(map(int, str(int_digits)))
    
    def plusOne2(self, digits: List[int]) -> List[int]:
        idx = len(digits)-1
        remainder = 1


        while remainder>0 and idx >= 0:
            digits[idx] += remainder
            remainder = digits[idx] % 9

            if digits[idx]>9:
                digits[idx] = digits[idx] % 10
                remainder = 1
            else:
                remainder = 0
            idx -= 1
        
        if remainder == 1:
            digits.insert (0, remainder)
        return digits

               
print(Solution().plusOne2([1, 9, 9]))


