# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode])-> None:
        temp = head
        prev = None
        while head != None:
            head = head.next
            temp.next = prev
            prev = temp
            temp = head
        # temp.next = prev
        return prev
    def reorderList(self, head: Optional[ListNode]) -> None:
        count = 0
        temp = head
        while temp != None:
            count +=1
            temp = temp.next
        trav = (count -1) // 2
        temp = head
        i = 1
        while i<= trav:
            temp = temp.next
            i +=1
        p2 = self.reverseList(temp.next)
        temp.next = None

        p1 = head

        while p2:
            temp1 = p1.next
            temp2 = p2.next

            p1.next = p2
            p2.next = temp1

            p1 = temp1
            p2 = temp2
        
        