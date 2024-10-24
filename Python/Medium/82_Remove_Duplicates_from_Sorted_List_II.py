#  https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        previous_node = ListNode()
        prev_tail = previous_node
        current_node = head
        next_node = head.next

        duplicate_val = None

        while current_node is not None:
            if next_node is not None and current_node.val == next_node.val:
                duplicate_val = current_node.val
                current_node = next_node.next
            elif current_node.val==duplicate_val:
                current_node = current_node.next
            else:
                previous_node.next = ListNode(current_node.val)
                previous_node = previous_node.next
                current_node = current_node.next
            next_node = current_node.next if current_node is not None else None
        return prev_tail.next
    

head = ListNode(1, ListNode(1, ListNode(2, ListNode(5, ListNode(5)))))
# head = ListNode(1, ListNode(1, ListNode(2, None)))
# head = ListNode(1, ListNode(1, ListNode(2, None)))

Solution().deleteDuplicates(head)



                