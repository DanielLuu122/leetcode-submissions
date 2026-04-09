# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
#         n = len(nums)
#         sums = sum(nums)
#         if sums % 2 == 1:
#             return False
#         # divisible by 2
#         target = sum(nums) // 2
#         dp = [[False] * (target + 1) for _ in range(n)]
#         for j in range(target + 1):
#             if nums[0] == j:
#                 dp[0][j] = True
#         for i in range(1, n):
#             for j in range(target + 1):
#                 if nums[i] == j:
#                     dp[i][j] = True
#                 if j - nums[i] >= 0 and dp[i-1][j-nums[i]]:
#                     dp[i][j] = True
#                 dp[i][j] = dp[i-1][j] or dp[i][j]
#         return dp[n-1][target]
        
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        
        target = total // 2
        n = len(nums)
        
        # dp[i][j] = whether we can make sum j using first i elements
        dp = [[False] * (target + 1) for _ in range(n + 1)]
        
        # Base case: sum 0 can always be achieved with empty subset
        for i in range(n + 1):
            dp[i][0] = True
        
        # Fill the DP table
        for i in range(1, n + 1):
            for j in range(1, target + 1):
                # Option 1: Don't take nums[i-1]
                dp[i][j] = dp[i-1][j]
                
                # Option 2: Take nums[i-1] if it fits
                if j >= nums[i-1]:
                    dp[i][j] = dp[i][j] or dp[i-1][j - nums[i-1]]
        
        return dp[n][target]
