# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        carryOver = 0
        cur = None
        while l1 or l2 or carryOver:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            newVal = v1 + v2 + carryOver
            if newVal > 9:
                carryOver = 1
                newVal -= 10
            else:
                carryOver = 0
            new_node = ListNode(newVal)
            if head is None:
                head = new_node
                cur = new_node
            else:
                cur.next = new_node
                cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return head
        

