class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_needle = len(needle)
        max_loop = len(haystack) - len_needle + 1

        for search_idx in range(max_loop):
            if haystack[search_idx] == needle[0] and haystack[search_idx: search_idx+len_needle] == needle:
               return search_idx
        return -1


haystack = "hello"
needle = "ll"
print(Solution().strStr(haystack, needle))
