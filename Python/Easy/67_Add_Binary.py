# https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        remainder = 0

        idx_a = len(a) - 1
        idx_b = len(b) - 1
        sum_of_a_b = ""

        while idx_a>=0 or idx_b >=0:
            a_val = a[idx_a] if idx_a>=0 else 0
            b_val = b[idx_b] if idx_b>=0 else 0

            result = int(a_val) + int(b_val) + remainder

            remainder = 1 if result > 1 else 0
            result =  result % 2

            sum_of_a_b = str(result) + sum_of_a_b
            idx_a -= 1
            idx_b -= 1
            
        sum_of_a_b = str(remainder) + sum_of_a_b if remainder > 0 else sum_of_a_b
        return sum_of_a_b
    
    def addBinaryBetter(self, a: str, b: str) -> str:
        sum = int(a,2) + int(b,2)
        return "{:b}".format(sum)
    
a = "111"
b = "111111"
print(Solution().addBinary(a, b))


