class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # val -> longest consecutive starting from val
        m = 0
        seen = set()
        for val in nums:
            seen.add(val)

        for val in seen:
            count = 1
            if val - 1 in seen:
                continue
            temp = val + 1
            while temp in seen:
                count += 1
                temp += 1
            m = max(count, m)
        return m
        