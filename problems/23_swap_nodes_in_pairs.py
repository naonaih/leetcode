# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newList = ListNode()
        result = newList

        #headの中身が0個もしくは1個だけだったときの処理
        if head == None or head.next == None :
            return head

        while head.next != None:
            #headの現在と次のListNodeを入れ替えてnewListに保zん
            newList.next = ListNode(head.next.val)
            newList = newList.next
            print(head.val)
            newList.next = ListNode(head.val)
            newList = newList.next

            #headは二個進める
            head = head.next
            head = head.next

            #2個先がからだった場合の処理
            if head == None:
               break

        #headの長さが奇数で1つだけ余った場合は、それをnewListに入れる
        if head != None and head.next == None:
            newList.next = ListNode(head.val)

        return result.next

