# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_list = []
        l2_list = []

        while l1:
            l1_list = [str(l1.val)] + l1_list
            l1 = l1.next

        while l2:
            l2_list = [str(l2.val)] + l2_list
            l2 = l2.next

        l1_num = int(''.join(l1_list))
        l2_num = int(''.join(l2_list))

        l_sum = str(l1_num + l2_num)

        # create ans linked lists
        dummy = ListNode(val=None)
        ans = dummy

        for i in range(len(l_sum) - 1, -1, -1):
            dummy.next = ListNode(val=int(l_sum[i]))
            dummy = dummy.next

        return ans.next
