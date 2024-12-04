# https://leetcode.com/problems/climbing-stairs/
import sys

from pathlib import Path

PATH = Path(__file__).resolve().parents[2]
sys.path.append(str(PATH))

from Python.Utils.Tree import Tree

class Solution:
    def climbStairs(self, n: int) -> int:
        root = Tree(0)
        step_count = 0
        queue = [root]

        while queue:
            popped = queue.pop(0)
            val = popped.value

            if not popped.left:
                
                if val < n-1:
                    popped.left = Tree(val)
                    queue.append(popped.left)
                elif val == n:
                    step_count += 1

            if not popped.right:
                if val < n-2:
                    popped.right = Tree(val)
                    queue.append(popped.right)
                elif val == n:
                    step_count += 1
        return step_count
    

print(Solution().climbStairs(5))
            
