# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        current_node = head
        next_node = head.next


        while next_node is not None:
            if next_node.val == current_node.val:
                current_node.next = next_node.next
            else:
                current_node = current_node.next
            next_node = current_node.next if current_node is not None else None

        return head
    

head = ListNode(1, ListNode(1, ListNode(1, None)))
Solution().deleteDuplicates(head)
                