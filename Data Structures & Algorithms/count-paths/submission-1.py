class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # [1] * n creates ONE row with n items
        # Example: n = 4 -> [1, 1, 1, 1]

        # The outer loop repeats that row m times
        # Example: m = 3, n = 4 ->
        # [
        #   [1, 1, 1, 1],
        #   [1, 1, 1, 1],
        #   [1, 1, 1, 1]
        # ]
        dp = [[1] * n for _ in range(m)]

        # Start from row 1 because row 0 already has only 1 way
        for row in range(1, m):

            # Start from col 1 because col 0 already has only 1 way
            for col in range(1, n):

                # dp[row][col] = current box
                #
                # row - 1 = box ABOVE
                # col - 1 = box to the LEFT
                #
                # We can only arrive from above or left,
                # so add those two numbers.
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

        # m - 1 and n - 1 give the last row and last column
        # This is the bottom-right box
        return dp[m - 1][n - 1]