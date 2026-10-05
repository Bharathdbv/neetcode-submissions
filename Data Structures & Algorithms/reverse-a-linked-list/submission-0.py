# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # print(head)
        # print(head.val)
        # print(head.next)
        temp = head
        prev = None
        while head != None:
            head = head.next
            temp.next = prev
            prev = temp
            temp = head
        # temp.next = prev
        return prev