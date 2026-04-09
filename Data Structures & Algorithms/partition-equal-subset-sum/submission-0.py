class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        sums = sum(nums)
        if sums % 2 == 1:
            return False
        # divisible by 2
        target = sum(nums) // 2
        dp = [[False] * (target + 1) for _ in range(n)]
        for j in range(target + 1):
            if nums[0] == j:
                dp[0][j] = True
        for i in range(n):
            for j in range(target + 1):
                if nums[i] == j:
                    dp[i][j] = True
                if j - nums[i] >= 0 and dp[i-1][j-nums[i]]:
                    dp[i][j] = True
                dp[i][j] = dp[i-1][j] or dp[i][j]
        return dp[n-1][target]

