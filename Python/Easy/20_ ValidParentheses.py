# https://leetcode.com/problems/valid-parentheses/description/

class Solution:   
    def isValidMySoln(self, s: str) -> bool:
        pair = {'(': ')', '[': ']', '{': '}'}
        len_string = len(s)

        stack = []
        stack_idx = -1
        idx = 0

        while idx < len_string:
            start_val = s[idx]
            expected_end_val = pair.get(start_val)

            if idx < len_string-1 and s[idx+1] == expected_end_val:
                idx +=2
            elif stack_idx>=0 and pair.get(stack[stack_idx]) == start_val:
                stack.pop()
                stack_idx -= 1
                idx +=1
            else:
                stack.append(start_val)
                idx += 1
                stack_idx += 1

        if stack_idx == -1 and len_string>0:
            return True
        return False
    

    def isValidOtherSolns(self, s: str) -> bool:
        stack=[]
        d={'(':')','{':'}','[':']'}
        for i in s:
            if i in d:
                stack.append(i)
            elif len(stack)==0 or i!=d[stack.pop()]:
                return False
        return len(stack)==0

s = '()[]{})'
s = '()'
s = "([])"
s = "("
s = "(([]){})"
val = Solution().isValidOtherSolns(s)

print(val)
