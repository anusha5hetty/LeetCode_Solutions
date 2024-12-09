# https://leetcode.com/problems/add-two-numbers/
import sys

from pathlib import Path
from typing import Optional
from math import floor

PATH = Path(__file__).resolve().parents[2]
sys.path.append(str(PATH))

from Python.Utils.ListNode import ListNode

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry_forward = 0
        result = ListNode(0)
        traversal = result

        while l1 is not None and l2 is not None:
            sum1 = l1.val + l2.val + carry_forward
            to_add = sum1 % 10
            carry_forward = floor(sum1/10)
            traversal.next = ListNode(to_add)
            traversal = traversal.next
            l1 = l1.next
            l2 = l2.next
        
        while l1 is not None:
            sum1 = l1.val + carry_forward
            to_add = sum1 % 10
            carry_forward = floor(sum1/10)
            traversal.next = ListNode(to_add)
            traversal = traversal.next
            l1 = l1.next

        while l2 is not None:
            sum1 = l2.val + carry_forward
            to_add = sum1 % 10
            carry_forward = floor(sum1/10)
            traversal.next = ListNode(to_add)
            traversal = traversal.next
            l2 = l2.next
        
        if carry_forward > 0:
            traversal.next = ListNode(carry_forward)

        return result.next
    
    def addTwoNumbersBetter(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry_forward = 0
        result = ListNode(0)
        traversal = result

        while l1 or l2 or carry_forward:
            sum1 = carry_forward
            if l1 is not None:
                sum1 += l1.val
                l1 = l1.next
            if l2 is not None:
                sum1 += l2.val
                l2 = l2.next

            to_add = sum1 % 10
            carry_forward = floor(sum1/10)
            traversal.next = ListNode(to_add)
            traversal = traversal.next

        return result.next

# [2,4,3]
# [5,6,4]

l1 = ListNode(2,
                ListNode(4,
                            ListNode(3)))

l2 = ListNode(5, 
                ListNode(6,
                            ListNode(4)))

Solution().addTwoNumbers(l1, l2)