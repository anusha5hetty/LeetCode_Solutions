# https://leetcode.com/problems/reverse-vowels-of-a-string

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        point1 = 0
        point2 = len(s)-1
        lst_char = list(s)

        while point1 <= point2:
            if lst_char[point1] in vowels and lst_char[point2] in vowels:
                temp = lst_char[point1]
                lst_char[point1] = lst_char[point2]
                lst_char[point2] = temp

                point1 += 1
                point2 -= 1
                continue
            
            if lst_char[point1] not in vowels:
                point1 += 1

            if lst_char[point2] not in vowels:
                point2 -= 1
        return ''.join(lst_char)



s = ".a"

s = Solution().reverseVowels(s)
print(s)