class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = ""
        char_found = False

        idx = len(s)-1

        while idx>=0:
            x = s[idx]
            if char_found and x == " ":
                return len(word)
            elif x is not None and x != " " and x !="":
                char_found = True
                word += x
            idx -=1

        return len(word)

    def lengthOfLastWordBetterSoln(self, s: str) -> int:
        length = 0
        x = s.strip()

        for i in range(len(x) - 1, -1, -1):
            if x[i] != " ":
                length += 1
            else:  
                break
        
        return length

s = "Hello"
print(Solution().lengthOfLastWord(s))