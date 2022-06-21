# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newList = ListNode()
        result = newList
        s = set()

        while head != None:

            print(s)

            # if head val did not appear until now, add to new list
            if head.val not in s:
                print(head.val)

                s.add(head.val)
                newList.next = ListNode(head.val)
                newList = newList.next

            # proceed to next node
            head = head.next

        return result.next