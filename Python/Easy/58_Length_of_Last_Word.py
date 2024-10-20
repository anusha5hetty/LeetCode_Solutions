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
        s = s.rstrip()  # Remove trailing spaces
        length = 0

        for char in reversed(s):
            if char == " ":
                break
            length += 1

        return length

s = "Hello"
print(Solution().lengthOfLastWord(s))