# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        pre = None

        while head != None:
            reverse = ListNode(val=head.val)
            reverse.next = pre
            pre = reverse
            head = head.next

        return reverse