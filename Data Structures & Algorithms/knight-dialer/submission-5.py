class Solution:
    def knightDialer(self, n: int) -> int:
        mp = {}
        mp[0] = [4, 6]
        mp[1] = [6, 8]
        mp[2] = [7, 9]
        mp[3] = [4, 8]
        mp[4] = [3, 9, 0]
        mp[5] = []
        mp[6] = [1, 7, 0]
        mp[7] = [2, 6]
        mp[8] = [1, 3]
        mp[9] = [2, 4]
        # initial length 1 for all digits n = 1
        dp = [1] * 10
        for i in range(1, n):
            new_dp = [0] * 10
            for i in range(10):
                for e in mp[i]: 
                    new_dp[i] += dp[e]
                    new_dp[i] = new_dp[i] % 1000000007
            dp = new_dp
        return sum(dp) % 1000000007




