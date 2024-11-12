# https://leetcode.com/problems/pascals-triangle-ii/

from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev_row = [1]

        for _ in range(rowIndex):
            temp = [0] + prev_row + [0]
            new_row = []
            for count in range(len(temp)-1):
                new_row.append(temp[count] + temp[count+1])
            
            prev_row = new_row

        return prev_row
    
print(Solution().getRow(5))