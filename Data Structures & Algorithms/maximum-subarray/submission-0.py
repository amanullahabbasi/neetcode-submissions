class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = nums[0]
        best = nums[0]

        for i in range(1, len(nums)):
            n = nums[i]
            if current + n > n:
                current = current + n
            else:
                current = n
            if current > best:
                best = current

        return best