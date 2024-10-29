#  https://leetcode.com/problems/integer-to-roman/description/

import math

class Solution:
    def intToRoman(self, num: int) -> str:
        mapping = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        len_num = len(str(num))
        roman = ''
        multiple = int(math.pow(10, len_num-1))

        while multiple>=1:
            val = num//multiple

            if val == 5 or val == 10:
                roman += mapping[val*multiple]
            
            elif val == 4 or val == 9:
                roman += mapping[multiple] + mapping[(val+1)*multiple]
            
            elif val<4 or val < 9:
                if not val < 4:
                    roman += mapping[5*multiple]
                    val = val - 5
                symbol = mapping[multiple]
                roman += (symbol*val)

            num = num % multiple
            multiple = multiple // 10
        return roman
    
    def intToRomanOther(self, num: int) -> str:
        num_map = {
        1: "I",
        5: "V",    4: "IV",
        10: "X",   9: "IX",
        50: "L",   40: "XL",
        100: "C",  90: "XC",
        500: "D",  400: "CD",
        1000: "M", 900: "CM",
        }
        
        # Result Variable
        r = ''
        
        
        for n in sorted(num_map.keys(),reverse=True):
            # If n in list then add the roman value to result variable
            while n <= num:
                r += num_map[n]
                num-=n
        return r


num = 3498
                
print(Solution().intToRoman(num))
print(Solution().intToRomanOther(num))





