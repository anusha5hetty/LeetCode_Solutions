#  https://leetcode.com/problems/plus-one/

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        idx = len(digits)-1

        digits[idx] += 1
        remainder = digits[idx] % 9

        while remainder>0 and idx > 0:
            idx -= 1
            digits[idx] = digits[idx] + remainder

            if digits[idx]>9:
                digits[idx] = digits[idx] % 10
                remainder = 1
            else:
                remainder = 0
            
        
        if remainder>0:
            return [remainder].extend(digits)
        else :
            return digits

            

    
    def plusOne2(self, digits: List[int]) -> List[int]:
        str_digits = ''.join(map(str, digits))
        int_digits = int(str_digits) + 1
        return list(map(int, str(int_digits)))
    
print(Solution().plusOne([9, 9]))


