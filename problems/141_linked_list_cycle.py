# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        max_count = 10 ** 4 + 10
        cnt = 0
        if head == None:
            return False

        while head:
            head = head.next
            cnt += 1
            if cnt == max_count:
                return True

        return False
