class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [[0] * 2 for x in range(n)]
        dp[0][1] = nums[0]
        dp[0][0] = nums[0]
        for i in range(1,n):
            dp[i][1] = max((dp[i - 1][1] + nums[i]), nums[i])
            dp[i][0] = max(dp[i-1][1], dp[i-1][0])
        print(dp)
        return max(dp[n - 1][1], dp[n-1][0])