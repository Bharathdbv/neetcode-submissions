# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # if n == 1:
        #     return head.next
        x = head
        count = 0
        while x!= None:
            count+=1
            x = x.next
        print(count)
        i = 1
        temp = head
        trav = head
        k = count - n +1
        if k == 1:
            return temp.next
        while i<k:
            if i!=1:
                temp = temp.next
            trav = trav.next
            i += 1
        temp.next = trav.next
        return head
