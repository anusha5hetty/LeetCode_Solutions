# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def add_last(self, node: ListNode):
#         if self.head is None:
#             self.head = node
#             self.tail = node
#         else:
#             self.tail.next = node
#             self.tail = node

#     def traverse(self):
#         valx = self.head
#         while valx is not None:
#             print(valx.val)
#             valx = valx.next



class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        lst1_pointer = list1
        lst2_pointer = list2
        list3 = ListNode()
        list3_tail = list3

        while lst1_pointer is not None and lst2_pointer is not None:
            if lst1_pointer.val < lst2_pointer.val:
                to_add = lst1_pointer
                lst1_pointer = lst1_pointer.next
            else:
                to_add = lst2_pointer
                lst2_pointer = lst2_pointer.next

            list3_tail.next = ListNode(to_add.val)
            list3_tail = list3_tail.next
            
        list3_tail.next = lst1_pointer if lst1_pointer else lst2_pointer
        
        return list3.next

