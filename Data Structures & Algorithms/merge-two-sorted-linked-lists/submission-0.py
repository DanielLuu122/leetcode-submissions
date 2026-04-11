# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        curr = None
        l1 = list1
        l2 = list2
        while l1 or l2:
            if l1 == None:
                if head == None:
                    head = l2
                else:
                   curr.next = l2
                curr = l2
                l2 = l2.next
            elif l2 == None:
                if head == None:
                    head = l1
                else:
                   curr.next = l1
                curr = l1
                l1 = l1.next
            elif l1.val < l2.val:
                if head == None:
                    head = l1
                else:
                   curr.next = l1
                curr = l1
                l1 = l1.next
            else:
                if head == None:
                    head = l2
                else:
                   curr.next = l2
                curr = l2
                l2 = l2.next
        return head
