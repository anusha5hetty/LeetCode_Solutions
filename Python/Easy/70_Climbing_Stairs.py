# https://leetcode.com/problems/climbing-stairs/
from collections import deque

import sys

from pathlib import Path

PATH = Path(__file__).resolve().parents[2]
sys.path.append(str(PATH))

from Python.Utils.Tree import Tree

class Solution:
    def climbStairs(self, n: int) -> int:
        root = Tree(0)
        step_count = 0
        # Queue because we are using BFS for adding items to the Tree
        queue = deque([root])

        while queue:
            popped = queue.pop()
            val = popped.value

            if val == n:
                step_count += 1
            else:
                if (not popped.left) and val < n:
                    popped.left = Tree(val+1)
                    queue.appendleft(popped.left)
                if (not popped.right) and val < n-1:
                    popped.right = Tree(val+2)
                    queue.appendleft(popped.right)
               
        return step_count
        

print(Solution().climbStairs(5))
            
