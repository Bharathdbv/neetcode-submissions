# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        nl = None
        head = None
        while list1 != None and list2!= None:
            if list1.val <= list2.val:
                x = list1.val
                if nl == None:
                    nl = ListNode(x)
                    head = nl
                else:
                    nn = ListNode(x)
                    nl.next = nn
                    nl = nn
                list1 = list1.next
            else:
                y = list2.val
                if nl == None:
                    nl = ListNode(y)
                    head = nl
                else:
                    nn = ListNode(y)
                    nl.next = nn
                    nl = nn
                list2 = list2.next
        while list1 != None:
            x = list1.val
            if nl == None:
                nl = ListNode(x)
                head = nl
            else:
                nn = ListNode(x)
                nl.next = nn
                nl = nn
            list1 = list1.next
        while list2 != None:
            x = list2.val
            if nl == None:
                nl = ListNode(x)
                head = nl
            else:
                nn = ListNode(x)
                nl.next = nn
                nl = nn
            list2 = list2.next
        
        return head