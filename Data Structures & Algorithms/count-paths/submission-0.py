class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # dp[row][col] = number of ways to reach this box
        dp = [[1] * n for _ in range(m)]

        # Skip first row and first column because they already stay 1
        for row in range(1, m):
            for col in range(1, n):

                # Ways to reach current box =
                # ways from above + ways from left
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

        # Bottom-right box contains final answer
        return dp[m - 1][n - 1]