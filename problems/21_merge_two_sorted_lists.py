# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newList = ListNode()
        result = newList

        while(list1 != None and list2 != None):

            if list1.val < list2.val:
                newList.next = ListNode(list1.val)
                newList = newList.next
                list1 = list1.next
            else:
                newList.next = ListNode(list2.val)
                newList = newList.next
                list2 = list2.next

        if list1 == None:
            while list2 != None:
                newList.next = ListNode(list2.val)
                newList = newList.next
                list2 = list2.next

        if list2 == None:
            while list1 != None:
                newList.next = ListNode(list1.val)
                newList = newList.next
                list1 = list1.next

        return result.next
