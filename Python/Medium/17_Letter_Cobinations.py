# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
from typing import List

class Solution:
    def __init__(self):
        self.combination = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], 
                            '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], 
                            '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}

    def letterCombinations(self, digits: str) -> List[str]:
        # second method that takes 2 parameters - first - list of existing combination, second - list of char to be combined.
        new_combination = []
        for digit in digits:
            if not new_combination:
                new_combination = self.combination[digit]
            else:
                new_combination = self.combine(new_combination, digit)
        return new_combination

    def combine(self, combination: List[str], digit: str) -> List[str]:
        new_combination = []
        for char in self.combination[digit]:
            for comb in combination:
                new_combination.append(comb+char)
        return new_combination
    
class Solution2:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        def backtrack(i, combo):
            if i == len(digits):
                res.append(combo)
                return
            
            for letter in digit_to_letters[digits[i]]:
                backtrack(i + 1, combo + letter)

        res = []
        backtrack(0, "")

        return res


digits = "256"
Solution2().letterCombinations(digits)
print("fsf")
# The backtrack method is called recursively for each digit in the input string.
# Complete combination is built by adding one letter at a time to the current combination.
# Once the combination is complete, it is added to the result list.
# The backtrack method takes the digit index and the current combination as input. 
# The Time complexity is O(3^N * 4^M) where N is the number of digits in the input that maps to 3 letters and M is the number of digits in the input that maps to 4 letters.