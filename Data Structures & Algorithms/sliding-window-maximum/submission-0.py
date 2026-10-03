from sortedcontainers import SortedList

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        curr = SortedList()
        
        for i in range(k):
            curr.add(nums[i])
        
        ans = [curr[-1]]
        l = 0
        for r in range(k, len(nums)):
            curr.remove(nums[l])
            curr.add(nums[r])
            ans.append(curr[-1])
            l += 1
        return ans