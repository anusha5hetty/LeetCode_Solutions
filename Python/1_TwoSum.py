# https://leetcode.com/problemset/
# https://leetcode.com/problems/two-sum/description/
from typing import List

class Solution:

    def longestCommonPrefixMySolution(self, strs: List[str]) -> str:
        output = ""

        if len(strs) == 0 or len(strs[0]) == 0:
            return output
        
        for idx in range(200):
            try:
                letter = strs[0][idx]

                for string in strs:
                    if string == "" or (len(string) <= idx) or (string[idx] != letter):
                        return output

                output += letter
            except Exception:
                return output

    def longestCommonPrefixBestSolution(self, strs: List[str]) -> str:
        strs = sorted(strs)
        result = ""
        first = strs[0]
        last = strs[-1]
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return result
            result += first[i]
        return result
