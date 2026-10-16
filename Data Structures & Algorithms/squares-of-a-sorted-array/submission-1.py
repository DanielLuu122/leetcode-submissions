class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        l = 0
        r = n - 1
        idx = n - 1
        # print(res)
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                res[idx] = nums[l] * nums[l]
                l += 1
            else:
                res[idx] = nums[r] * nums[r]
                r -= 1
            idx -= 1
        return res
