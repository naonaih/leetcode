# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        reverse = ListNode()
        result = reverse
        num = []
        while head != None:
            num.append(head.val)
            head = head.next

        for i in range(len(num) - 1, -1, -1):
            reverse.val = num[i]
            if i != 0:
                reverse.next = ListNode()
                reverse = reverse.next
        return result

