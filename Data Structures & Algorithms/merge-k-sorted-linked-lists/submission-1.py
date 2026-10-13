# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        head = None
        prev = None
        heap = [] 
        # 1 -> 2
        # 2 -> 4
        # 3 -> 5
        for i in range(len(lists)):
            if lists[i] is not None:
                heapq.heappush(heap, (lists[i].val, i))

        # (2, 1), (2, 2), (3, 3)
        while heap:
            # idx = index of the list it came from
            smallest_val, idx = heapq.heappop(heap) # O(1)
            node = lists[idx]
            lists[idx] = lists[idx].next
            if lists[idx]is not None:
                heapq.heappush(heap, (lists[idx].val, idx))

            if not prev:
                head = node
                prev = node
                # 1
            else:
                # 1 -> 2 -> 2 -> 4
                prev.next = node # adds element to list 
                prev = prev.next # shift tail ptr by 1 
        
        return head