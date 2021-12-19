# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        keta = 1
        n1 = 0
        cur = l1
        while cur != None:
            n1 += cur.val * keta
            keta *= 10
            cur = cur.next
       
        keta = 1
        n2 = 0
        cur = l2
        while cur != None:
            n2 += cur.val * keta
            keta *= 10
            cur = cur.next
       
        
        newList = ListNode()
        result = newList
        
        s = n1 + n2
        s = list(str(s))
        print(s)
        
        
        for x in s[::-1]:
            newList.next = ListNode(x)
            newList = newList.next
        
        return result.next
            