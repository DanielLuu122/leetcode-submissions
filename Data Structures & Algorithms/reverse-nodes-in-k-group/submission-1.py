# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        buff = []
        cur = head
        count = 0
        dummy = ListNode(0, head)
        prev_group = dummy
        while cur:
            #print(cur.val)
            buff.append(cur)
            cur = cur.next
            count += 1
            if count == k:
                for i in range(k - 1, 0, -1):
                    buff[i].next = buff[i-1]
                buff[0].next = cur
                prev_group.next = buff[k-1]
                prev_group = buff[0]
                count = 0
                buff = []
        return dummy.next


