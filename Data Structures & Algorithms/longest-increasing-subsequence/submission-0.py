class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] = best increasing sequence ending at index i
        dp = [1] * len(nums)

        for current in range(len(nums)):
            for previous in range(current):

                if nums[previous] < nums[current]:
                    new_length = dp[previous] + 1
                    dp[current] = max(dp[current], new_length)

        return max(dp)