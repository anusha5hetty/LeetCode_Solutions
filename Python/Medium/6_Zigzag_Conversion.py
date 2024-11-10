# https://leetcode.com/problems/zigzag-conversion/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        dct_rows = {}
        increment = False
        string = ""
        key = 0

        for _, val in enumerate(s):
            if(dct_rows.get(key)):
                dct_rows[key].append(val)
            else:
                dct_rows[key] = [val]

            if key == (numRows-1) or key==0:
                increment = not increment

            key = key + 1 if increment else key - 1

        for idx in range(len(dct_rows)):
            string += "".join(dct_rows[idx])

        return string
    
    def convertOtherSolution(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows > len(s):
            return s
        rows = ['']*numRows
        going_down = False
        current_row = 0

        for char in s:
            rows[current_row]+=char
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            current_row +=1 if going_down else -1
        
        return ''.join(rows)
    
numRows = 3
s = "PAYPALISHIRING"
# s= "A"
Solution().convertOtherSolution(s, numRows)
