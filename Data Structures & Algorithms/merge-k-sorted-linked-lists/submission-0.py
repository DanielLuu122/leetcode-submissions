# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []
        l = 0
        for i in range(len(lists)):
            if lists[i] is not None:
                heapq.heappush(h, (lists[i].val, l, lists[i]))
                l += 1
        dummy = ListNode(0)
        curr = dummy
        
        while h:
            _, _, nxt = heapq.heappop(h)
            curr.next = nxt
            if nxt.next:
                heapq.heappush(h, (nxt.next.val, l, nxt.next))
                l += 1
            curr = nxt
        return dummy.next



        